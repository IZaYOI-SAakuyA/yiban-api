#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getopt
import json
import os
import random
import re
import sys
import time
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import ybtopic
import ybvote
#import ybfeed
from yblogin import BASEURL, getInfo, getUserToken


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(901, 601)
        mainWindow.setMinimumSize(QtCore.QSize(451, 301))
        mainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineedit.setObjectName("usernameLineedit")
        self.formLayout_4.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.usernameLineedit)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineedit.setObjectName("passwordLineedit")
        self.formLayout_4.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.passwordLineedit)
        self.lauchButton = QtWidgets.QPushButton(self.centralwidget)
        self.lauchButton.setObjectName("lauchButton")
        self.formLayout_4.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.lauchButton)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.voteformLayout = QtWidgets.QFormLayout()
        self.voteformLayout.setObjectName("voteformLayout")
        self.add_vote_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.add_vote_countLabel.setObjectName("add_vote_countLabel")
        self.voteformLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.add_vote_countLabel)
        self.add_vote_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.add_vote_countSpinbox.setProperty("value", 1)
        self.add_vote_countSpinbox.setObjectName("add_vote_countSpinbox")
        self.voteformLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.add_vote_countSpinbox)
        self.vote_control_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.vote_control_countLabel.setObjectName("vote_control_countLabel")
        self.voteformLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.vote_control_countLabel)
        self.vote_control_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.vote_control_countSpinbox.setProperty("value", 2)
        self.vote_control_countSpinbox.setObjectName(
            "vote_control_countSpinbox")
        self.voteformLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.vote_control_countSpinbox)
        self.vote_reply_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.vote_reply_countLabel.setObjectName("vote_reply_countLabel")
        self.voteformLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.vote_reply_countLabel)
        self.vote_reply_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.vote_reply_countSpinbox.setProperty("value", 1)
        self.vote_reply_countSpinbox.setObjectName("vote_reply_countSpinbox")
        self.voteformLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.vote_reply_countSpinbox)
        self.gridLayout_2.addLayout(self.voteformLayout, 0, 0, 1, 1)
        self.choiceverticalLayout = QtWidgets.QVBoxLayout()
        self.choiceverticalLayout.setObjectName("choiceverticalLayout")
        self.voteCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.voteCheckbox.setIconSize(QtCore.QSize(10, 10))
        self.voteCheckbox.setChecked(True)
        self.voteCheckbox.setObjectName("voteCheckbox")
        self.choiceverticalLayout.addWidget(self.voteCheckbox)
        self.vote_upCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.vote_upCheckbox.setTabletTracking(False)
        self.vote_upCheckbox.setChecked(True)
        self.vote_upCheckbox.setObjectName("vote_upCheckbox")
        self.choiceverticalLayout.addWidget(self.vote_upCheckbox)
        self.vote_replyCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.vote_replyCheckbox.setChecked(True)
        self.vote_replyCheckbox.setObjectName("vote_replyCheckbox")
        self.choiceverticalLayout.addWidget(self.vote_replyCheckbox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.choiceverticalLayout.addWidget(self.line)
        self.topic_upCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.topic_upCheckbox.setChecked(True)
        self.topic_upCheckbox.setObjectName("topic_upCheckbox")
        self.choiceverticalLayout.addWidget(self.topic_upCheckbox)
        self.topic_replyCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.topic_replyCheckbox.setChecked(True)
        self.topic_replyCheckbox.setObjectName("topic_replyCheckbox")
        self.choiceverticalLayout.addWidget(self.topic_replyCheckbox)
        self.gridLayout_2.addLayout(self.choiceverticalLayout, 0, 2, 1, 1)
        self.topicformLayout = QtWidgets.QFormLayout()
        self.topicformLayout.setObjectName("topicformLayout")
        self.add_topic_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.add_topic_countLabel.setObjectName("add_topic_countLabel")
        self.topicformLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.add_topic_countLabel)
        self.add_topic_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.add_topic_countSpinbox.setProperty("value", 1)
        self.add_topic_countSpinbox.setObjectName("add_topic_countSpinbox")
        self.topicformLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.add_topic_countSpinbox)
        self.topic_control_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.topic_control_countLabel.setObjectName("topic_control_countLabel")
        self.topicformLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.topic_control_countLabel)
        self.topic_control_countSpinbox = QtWidgets.QSpinBox(
            self.centralwidget)
        self.topic_control_countSpinbox.setProperty("value", 2)
        self.topic_control_countSpinbox.setObjectName(
            "topic_control_countSpinbox")
        self.topicformLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.topic_control_countSpinbox)
        self.topic_reply_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.topic_reply_countSpinbox.setProperty("value", 1)
        self.topic_reply_countSpinbox.setObjectName("topic_reply_countSpinbox")
        self.topicformLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.topic_reply_countSpinbox)
        self.topic_reply_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.topic_reply_countLabel.setObjectName("topic_reply_countLabel")
        self.topicformLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.topic_reply_countLabel)
        self.gridLayout_2.addLayout(self.topicformLayout, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.catLabel = QtWidgets.QLabel(self.centralwidget)
        self.catLabel.setObjectName("catLabel")
        self.formLayout_3.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.catLabel)
        self.gridLayout_3.addLayout(self.formLayout_3, 2, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 3, 0, 1, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.comboBox.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "yiban"))
        self.usernameLabel.setText(_translate("mainWindow", "账号/手机号"))
        self.usernameLineedit.setText(_translate("mainWindow", ""))
        self.passwordLabel.setText(_translate("mainWindow", "密码"))
        self.passwordLineedit.setText(
            _translate("mainWindow", ""))
        self.lauchButton.setText(_translate("mainWindow", "启动"))
        self.add_vote_countLabel.setText(_translate("mainWindow", "发起投票数量"))
        self.vote_control_countLabel.setText(
            _translate("mainWindow", "投票互动数量"))
        self.vote_reply_countLabel.setText(_translate("mainWindow", "回复投票次数"))
        self.voteCheckbox.setText(_translate("mainWindow", "开启参与投票"))
        self.vote_upCheckbox.setText(_translate("mainWindow", "开启投票点赞"))
        self.vote_replyCheckbox.setText(_translate("mainWindow", "开启回复投票"))
        self.topic_upCheckbox.setText(_translate("mainWindow", "开启话题点赞"))
        self.topic_replyCheckbox.setText(_translate("mainWindow", "开启回复话题"))
        self.add_topic_countLabel.setText(_translate("mainWindow", "发起话题数量"))
        self.topic_control_countLabel.setText(
            _translate("mainWindow", "话题互动数量"))
        self.topic_reply_countLabel.setText(_translate("mainWindow", "回复话题次数"))
        self.comboBox.setCurrentText(_translate("mainWindow", "All - 随机"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Anime - 动画"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Comic – 漫画"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Game – 游戏"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Novel – 小说"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Myself – 原创"))
        self.comboBox.setItemText(5, _translate(
            "mainWindow", "Internet – 来自网络"))
        self.comboBox.setItemText(6, _translate("mainWindow", "Other – 其他"))
        self.comboBox.setItemText(7, _translate("mainWindow", "All - 随机"))
        self.catLabel.setText(_translate("mainWindow", "使用的文本内容"))


class MyThread(QtCore.QThread):

    def __init__(self, username, password, add_vote_count, vote_control_count, vote_reply_count, add_topic_count, topic_control_count, topic_reply_count, vote, vote_up, vote_reply, topic_up, topic_reply, cat):
        super(MyThread, self).__init__()
        self.username = username
        self.password = password
        self.add_vote_count = add_vote_count
        self.vote_control_count = vote_control_count
        self.vote_reply_count = vote_reply_count
        self.add_topic_count = add_topic_count
        self.topic_control_count = topic_control_count
        self.topic_reply_count = topic_reply_count
        self.vote = vote
        self.vote_up = vote_up
        self.vote_reply = vote_reply
        self.topic_up = topic_up
        self.topic_reply = topic_reply
        self.cat = cat

    def getHitokoto(self):
        cato = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "all",
        }
        Get_Hitokoto = r.get("https://sslapi.hitokoto.cn/",
                             params={"c": cato.get(self.cat), "encode": "json"}, timeout=10)
        Hitokoto = Get_Hitokoto.json()["hitokoto"]
        From = Get_Hitokoto.json()["from"]
        return Hitokoto + " --" + From

    def wait(self):
        self.getEPGA()
        # sleep#########################################################################################################################################
        return time.sleep(random.uniform(1, 3))

    def fprint(self, string, dlevel=0, num=0):
        dbglevel = {
            0: "",
            1: "I: ",
            2: "W: ",
            3: "E: "
        }
        if num > 0:
            number = " #" + str(num + 1)
        else:
            number = ""
        return dbglevel.get(dlevel) + string + number

    def login(self):
        try:
            self.sig.emit("账号: " + self.username)
            self.sig.emit("密码: " + self.password)
            yiban_user_token = getUserToken(self.username, self.password)
            self.sig.emit("易班 Token: " + yiban_user_token)
            self.token = dict(yiban_user_token=yiban_user_token)
            self.info = getInfo(self.token)
            self.group_id = self.info["group_id"]
            self.puid = self.info["puid"]
            self.channel_id = self.info["channel_id"]
            self.actor_id = self.info["actor_id"]
            self.nick = self.info["nick"]
            return self.sig.emit(self.fprint("登陆成功", dlevel=1))
        except:
            self.sig.emit(self.fprint("无法连接服务器或密码错误", dlevel=3))
            return self.stopsig.emit()
        finally:
            self.getEPGA()

    def getEPGA(self):
        try:
            Get_EPGA = r.get(BASEURL + "newgroup/indexPub/group_id/" +
                             self.group_id + "/puid/" + self.puid, cookies=self.token, timeout=10)
            EPGA = re.search(r"EGPA：[0-9\.]*", Get_EPGA.text)
            return self.epgasig.emit(EPGA.group())
        except:
            return self.epgasig.emit("无法连接服务器")
        finally:
            pass

    def runVote(self):
        self.prog = 50 / (int(self.add_vote_count) + int(self.vote_control_count)
                          * (self.vote / 2 + self.vote / 2 + self.vote_reply / 2 * int(self.vote_reply_count)))
        for i in range(0, int(self.add_vote_count)):
            try:
                response = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                ).add(
                    self.getHitokoto(),
                    self.getHitokoto(),
                    self.getHitokoto(),
                    self.getHitokoto()
                )
                self.sig.emit(self.fprint("添加投票 " + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加投票时未获取到的错误", dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(self.pro)
                self.wait()

        for i in range(0, int(self.vote_control_count)):
            try:
                self.vote_id = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                ).get(
                    self.vote_control_count
                )["data"]["list"][i]["id"]
                votego = ybvote.go(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.actor_id,
                    self.vote_id,
                    isOrganization=0,
                    ispublic=0
                )
                if self.vote:
                    try:
                        response = votego.vote(auto=True)
                        self.sig.emit(self.fprint(
                            "参与投票 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "参与投票时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.vote_up:
                    try:
                        response = votego.up()
                        self.sig.emit(self.fprint(
                            "点赞投票 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞投票时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.vote_reply:
                    for i in range(0, int(self.vote_reply_count)):
                        try:
                            response = votego.reply(self.getHitokoto())
                            self.sig.emit(self.fprint(
                                "添加投票评论 " + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加投票评论时未获取到的错误", dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(self.pro)
                            self.wait()
            except:
                self.sig.emit(self.fprint("获取投票列表时未获取到的错误", dlevel=2, num=i))
            finally:
                self.wait()

    def runTopic(self):
        self.prog = 50 / (int(self.add_topic_count) + int(self.topic_control_count) * (
            self.topic_up / 2 + self.topic_reply / 2 * int(self.topic_reply_count)))
        for i in range(0, int(self.add_topic_count)):
            try:
                response = ybtopic.topic(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.channel_id
                ).add(
                    self.getHitokoto(),
                    self.getHitokoto()
                )
                self.sig.emit(self.fprint("添加话题 " + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加话题时未获取到的错误", dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(self.pro)
                self.wait()
        for i in range(0, int(self.topic_control_count)):
            try:
                topicgo = ybtopic.topic(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.channel_id
                )
                self.article_id = topicgo.get(self.topic_control_count)[
                    "data"]["list"][i]["id"]
                if self.topic_up:
                    try:
                        response = topicgo.up(self.article_id)
                        self.sig.emit(self.fprint(
                            "点赞话题 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞话题时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.topic_reply:
                    for i in range(0, int(self.topic_reply_count)):
                        try:
                            response = topicgo.reply(
                                self.article_id, self.getHitokoto())
                            self.sig.emit(self.fprint(
                                "添加话题评论 " + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加话题评论时未获取到的错误", dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(self.pro)
                            self.wait()
            except:
                self.sig.emit(self.fprint("获取话题列表时未获取到的错误", dlevel=2, num=i))
            finally:
                self.wait()

    sig = QtCore.pyqtSignal(str)
    epgasig = QtCore.pyqtSignal(str)
    prosig = QtCore.pyqtSignal(int)
    stopsig = QtCore.pyqtSignal()

    def run(self):
        self.login()
        self.pro = 0
        self.runVote()
        self.prosig.emit(50)
        self.pro = 50
        self.runTopic()
        self.prosig.emit(100)
        r.close()


class MyWindow(QtWidgets.QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.lauchButton.released.connect(self.DisableButton)

    def DisableButton(self):
        self.plainTextEdit.appendPlainText("---运行开始---")
        self.lauchButton.setText("停止")
        self.lauchButton.setDisabled(True)
        self.usernameLineedit.setDisabled(True)
        self.passwordLineedit.setDisabled(True)
        self.add_vote_countSpinbox.setDisabled(True)
        self.vote_control_countSpinbox.setDisabled(True)
        self.vote_reply_countSpinbox.setDisabled(True)
        self.add_topic_countSpinbox.setDisabled(True)
        self.topic_control_countSpinbox.setDisabled(True)
        self.topic_reply_countSpinbox.setDisabled(True)
        self.voteCheckbox.setDisabled(True)
        self.vote_upCheckbox.setDisabled(True)
        self.vote_replyCheckbox.setDisabled(True)
        self.topic_upCheckbox.setDisabled(True)
        self.topic_replyCheckbox.setDisabled(True)
        self.comboBox.setDisabled(True)
        self.progressBar.setValue(0)

        self.mythread = MyThread(
            self.usernameLineedit.text(),
            self.passwordLineedit.text(),
            self.add_vote_countSpinbox.text(),
            self.vote_control_countSpinbox.text(),
            self.vote_reply_countSpinbox.text(),
            self.add_topic_countSpinbox.text(),
            self.topic_control_countSpinbox.text(),
            self.topic_reply_countSpinbox.text(),
            self.voteCheckbox.checkState(),
            self.vote_upCheckbox.checkState(),
            self.vote_replyCheckbox.checkState(),
            self.topic_upCheckbox.checkState(),
            self.topic_replyCheckbox.checkState(),
            self.comboBox.currentIndex()
        )
        self.mythread.sig.connect(self.PrintText)
        self.mythread.prosig.connect(self.Progress)
        self.mythread.epgasig.connect(self.EpgaShowup)
        self.mythread.stopsig.connect(self.StopThread)
        self.mythread.finished.connect(self.EnableButton)
        self.mythread.start()
        self.lauchButton.released.disconnect()
        self.lauchButton.released.connect(self.StopThread)
        self.lauchButton.setEnabled(True)

    def EnableButton(self):
        self.plainTextEdit.appendPlainText("---运行终止---")
        self.lauchButton.setText("启动")
        self.lauchButton.setDisabled(True)
        self.usernameLineedit.setEnabled(True)
        self.passwordLineedit.setEnabled(True)
        self.add_vote_countSpinbox.setEnabled(True)
        self.vote_control_countSpinbox.setEnabled(True)
        self.vote_reply_countSpinbox.setEnabled(True)
        self.add_topic_countSpinbox.setEnabled(True)
        self.topic_control_countSpinbox.setEnabled(True)
        self.topic_reply_countSpinbox.setEnabled(True)
        self.voteCheckbox.setEnabled(True)
        self.vote_upCheckbox.setEnabled(True)
        self.vote_replyCheckbox.setEnabled(True)
        self.topic_upCheckbox.setEnabled(True)
        self.topic_replyCheckbox.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.lauchButton.released.disconnect()
        self.lauchButton.released.connect(self.DisableButton)
        self.lauchButton.setEnabled(True)

    def StopThread(self):
        if self.mythread.isRunning():
            self.mythread.terminate()

    def EpgaShowup(self, string):
        # catLabel############################################################################################3
        self.catLabel.setText(string)

    def Progress(self, integer):
        self.progressBar.setValue(integer)

    def PrintText(self, string):
        self.plainTextEdit.appendPlainText(string)


if __name__ == "__main__":
    r = requests.Session()
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())
