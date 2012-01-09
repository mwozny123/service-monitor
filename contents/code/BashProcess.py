# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyKDE4.kdecore import *

class BashProcess(KProcess):
  
  PasswordError      = 11
  PermissionError    = 12

  def __init__(self, parent = None):
    KProcess.__init__(self, parent)
    self._errorType = None
    self._errorTypeMessage = None
    self._password = None
    self._command = ''

  def setSudoPassword(self, pw):
    self._password = pw

  def usesSudo(self):
    return self._password is not None

  def errorType(self):
    return self._errorType if self._errorType is not None else KProcess.error(self)

  def setBashCommand(self, command):
    command = command.replace('$INITDIR', self.guessInitDir())
    self._command = command

  def guessInitDir(self):
    return "/etc/rc.d" if QFile.exists("/etc/rc.d") else "/etc/init.d"

  def errorMessage(self):
    return self._errorTypeMessage

  def spitError(self, code, msg):
    self._errorType = code
    self._errorTypeMessage = msg
    self.terminate()
    self.close()
    self.error.emit(self.errorType())

  def start(self):

    # setup program
    # Der Parameter -D 8 sorgt für eine sofortige Ausgabe nach erfolgreicher Passworteingabe.
    # Ohne den Parameter hängt start() sonst so lange, bis das Hauptkommando ferig ist oder eine Ausgabe produziert.
    program = QStringList()
    if self.usesSudo():
      program << "/usr/bin/sudo" << "-kS" << "-D 8"
    program << "/bin/bash" << "-c" << self._command
    
    # start program
    self.setProgram(program)
    self.setProcessChannelMode(QProcess.SeparateChannels)
    KProcess.start(self)

    if self._password is not None:

      # listen on stderr, since sudo prints everything there
      self.setReadChannel(QProcess.StandardError)

      # start sudo, check if password prompt is present, then enter the password
      self.waitForReadyRead(); output = self.readAll()
      if not output.contains("password for"):
        return self.spitError(QProcess.FailedToStart, "please check your sudo installation")
      self.write("%s\n" % self._password)

      # wait for response and either issue an error or continue with normal process management
      self.waitForReadyRead(); output = self.readAll()
      if output.contains("try again"):
        return self.spitError(BashProcess.PasswordError, "wrong sudo password")
      elif output.contains("not in the sudoers file"):
        return self.spitError(BashProcess.PermissionError, "your user is not mentioned in the sudoers file")
