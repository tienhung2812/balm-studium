/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionAdd_Excel_file;
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *data_tab;
    QLabel *return_label;
    QLabel *liquidity_label;
    QTableWidget *liquidity_list;
    QLabel *cost_label;
    QPushButton *next_button;
    QTableWidget *cost_list;
    QTableWidget *return_list;
    QFrame *frame;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QTextEdit *textEdit;
    QTextEdit *textEdit_2;
    QTextEdit *textEdit_3;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QFrame *frame_2;
    QPushButton *pushButton_10;
    QPushButton *pushButton_11;
    QPushButton *pushButton_12;
    QTextEdit *textEdit_10;
    QLabel *label_10;
    QLabel *label_11;
    QTextEdit *textEdit_11;
    QLabel *label_12;
    QTextEdit *textEdit_12;
    QLabel *label_19;
    QTextEdit *textEdit_19;
    QFrame *frame_3;
    QPushButton *pushButton_19;
    QPushButton *pushButton_20;
    QPushButton *pushButton_21;
    QTextEdit *textEdit_21;
    QLabel *label_21;
    QLabel *label_22;
    QTextEdit *textEdit_22;
    QLabel *label_23;
    QTextEdit *textEdit_23;
    QLabel *label_24;
    QTextEdit *textEdit_24;
    QLabel *label_25;
    QTextEdit *textEdit_25;
    QWidget *contraint_tab;
    QPushButton *calculate_button;
    QTableWidget *contraint_table;
    QWidget *result_tab;
    QTableWidget *result_list;
    QLabel *objectiveFuntion_label;
    QLabel *objectiveFuntion_label_2;
    QMenuBar *menuBar;
    QMenu *menuFiles;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(915, 619);
        actionAdd_Excel_file = new QAction(MainWindow);
        actionAdd_Excel_file->setObjectName(QString::fromUtf8("actionAdd_Excel_file"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setEnabled(true);
        tabWidget->setGeometry(QRect(0, 10, 911, 571));
        data_tab = new QWidget();
        data_tab->setObjectName(QString::fromUtf8("data_tab"));
        return_label = new QLabel(data_tab);
        return_label->setObjectName(QString::fromUtf8("return_label"));
        return_label->setGeometry(QRect(720, 20, 59, 16));
        QFont font;
        font.setPointSize(15);
        return_label->setFont(font);
        return_label->setAlignment(Qt::AlignCenter);
        liquidity_label = new QLabel(data_tab);
        liquidity_label->setObjectName(QString::fromUtf8("liquidity_label"));
        liquidity_label->setGeometry(QRect(120, 20, 59, 16));
        liquidity_label->setFont(font);
        liquidity_list = new QTableWidget(data_tab);
        liquidity_list->setObjectName(QString::fromUtf8("liquidity_list"));
        liquidity_list->setGeometry(QRect(20, 40, 256, 321));
        cost_label = new QLabel(data_tab);
        cost_label->setObjectName(QString::fromUtf8("cost_label"));
        cost_label->setGeometry(QRect(400, 20, 59, 16));
        cost_label->setFont(font);
        cost_label->setAlignment(Qt::AlignCenter);
        next_button = new QPushButton(data_tab);
        next_button->setObjectName(QString::fromUtf8("next_button"));
        next_button->setGeometry(QRect(370, 500, 114, 32));
        next_button->setLayoutDirection(Qt::LeftToRight);
        next_button->setAutoFillBackground(false);
        cost_list = new QTableWidget(data_tab);
        cost_list->setObjectName(QString::fromUtf8("cost_list"));
        cost_list->setGeometry(QRect(300, 40, 256, 321));
        return_list = new QTableWidget(data_tab);
        return_list->setObjectName(QString::fromUtf8("return_list"));
        return_list->setGeometry(QRect(580, 40, 311, 321));
        frame = new QFrame(data_tab);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(20, 370, 256, 121));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(50, 90, 61, 32));
        pushButton_2 = new QPushButton(frame);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(170, 90, 81, 32));
        pushButton_3 = new QPushButton(frame);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(100, 90, 81, 32));
        textEdit = new QTextEdit(frame);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(10, 60, 71, 31));
        textEdit_2 = new QTextEdit(frame);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));
        textEdit_2->setGeometry(QRect(90, 60, 71, 31));
        textEdit_3 = new QTextEdit(frame);
        textEdit_3->setObjectName(QString::fromUtf8("textEdit_3"));
        textEdit_3->setGeometry(QRect(170, 60, 71, 31));
        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 10, 71, 51));
        QFont font1;
        font1.setPointSize(12);
        label->setFont(font1);
        label->setAlignment(Qt::AlignCenter);
        label->setWordWrap(true);
        label_2 = new QLabel(frame);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(90, 10, 71, 51));
        label_2->setFont(font1);
        label_2->setAlignment(Qt::AlignCenter);
        label_2->setWordWrap(true);
        label_3 = new QLabel(frame);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(170, 10, 71, 51));
        label_3->setFont(font1);
        label_3->setAlignment(Qt::AlignCenter);
        label_3->setWordWrap(true);
        frame_2 = new QFrame(data_tab);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setGeometry(QRect(300, 370, 256, 121));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        pushButton_10 = new QPushButton(frame_2);
        pushButton_10->setObjectName(QString::fromUtf8("pushButton_10"));
        pushButton_10->setGeometry(QRect(50, 90, 61, 32));
        pushButton_11 = new QPushButton(frame_2);
        pushButton_11->setObjectName(QString::fromUtf8("pushButton_11"));
        pushButton_11->setGeometry(QRect(170, 90, 81, 32));
        pushButton_12 = new QPushButton(frame_2);
        pushButton_12->setObjectName(QString::fromUtf8("pushButton_12"));
        pushButton_12->setGeometry(QRect(100, 90, 81, 32));
        textEdit_10 = new QTextEdit(frame_2);
        textEdit_10->setObjectName(QString::fromUtf8("textEdit_10"));
        textEdit_10->setGeometry(QRect(10, 60, 51, 31));
        label_10 = new QLabel(frame_2);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(10, 10, 51, 51));
        label_10->setFont(font1);
        label_10->setAlignment(Qt::AlignCenter);
        label_10->setWordWrap(true);
        label_11 = new QLabel(frame_2);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(70, 10, 51, 51));
        label_11->setFont(font1);
        label_11->setAlignment(Qt::AlignCenter);
        label_11->setWordWrap(true);
        textEdit_11 = new QTextEdit(frame_2);
        textEdit_11->setObjectName(QString::fromUtf8("textEdit_11"));
        textEdit_11->setGeometry(QRect(70, 60, 51, 31));
        label_12 = new QLabel(frame_2);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(130, 10, 51, 51));
        label_12->setFont(font1);
        label_12->setAlignment(Qt::AlignCenter);
        label_12->setWordWrap(true);
        textEdit_12 = new QTextEdit(frame_2);
        textEdit_12->setObjectName(QString::fromUtf8("textEdit_12"));
        textEdit_12->setGeometry(QRect(130, 60, 51, 31));
        label_19 = new QLabel(frame_2);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(185, 10, 61, 51));
        label_19->setFont(font1);
        label_19->setAlignment(Qt::AlignCenter);
        label_19->setWordWrap(true);
        textEdit_19 = new QTextEdit(frame_2);
        textEdit_19->setObjectName(QString::fromUtf8("textEdit_19"));
        textEdit_19->setGeometry(QRect(190, 60, 51, 31));
        frame_3 = new QFrame(data_tab);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setGeometry(QRect(580, 370, 311, 121));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        pushButton_19 = new QPushButton(frame_3);
        pushButton_19->setObjectName(QString::fromUtf8("pushButton_19"));
        pushButton_19->setGeometry(QRect(100, 90, 61, 32));
        pushButton_20 = new QPushButton(frame_3);
        pushButton_20->setObjectName(QString::fromUtf8("pushButton_20"));
        pushButton_20->setGeometry(QRect(220, 90, 81, 32));
        pushButton_21 = new QPushButton(frame_3);
        pushButton_21->setObjectName(QString::fromUtf8("pushButton_21"));
        pushButton_21->setGeometry(QRect(150, 90, 81, 32));
        textEdit_21 = new QTextEdit(frame_3);
        textEdit_21->setObjectName(QString::fromUtf8("textEdit_21"));
        textEdit_21->setGeometry(QRect(10, 60, 51, 31));
        label_21 = new QLabel(frame_3);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(10, 10, 51, 51));
        label_21->setFont(font1);
        label_21->setAlignment(Qt::AlignCenter);
        label_21->setWordWrap(true);
        label_22 = new QLabel(frame_3);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setGeometry(QRect(70, 10, 51, 51));
        label_22->setFont(font1);
        label_22->setAlignment(Qt::AlignCenter);
        label_22->setWordWrap(true);
        textEdit_22 = new QTextEdit(frame_3);
        textEdit_22->setObjectName(QString::fromUtf8("textEdit_22"));
        textEdit_22->setGeometry(QRect(70, 60, 51, 31));
        label_23 = new QLabel(frame_3);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(130, 10, 51, 51));
        label_23->setFont(font1);
        label_23->setAlignment(Qt::AlignCenter);
        label_23->setWordWrap(true);
        textEdit_23 = new QTextEdit(frame_3);
        textEdit_23->setObjectName(QString::fromUtf8("textEdit_23"));
        textEdit_23->setGeometry(QRect(130, 60, 51, 31));
        label_24 = new QLabel(frame_3);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(185, 10, 61, 51));
        label_24->setFont(font1);
        label_24->setAlignment(Qt::AlignCenter);
        label_24->setWordWrap(true);
        textEdit_24 = new QTextEdit(frame_3);
        textEdit_24->setObjectName(QString::fromUtf8("textEdit_24"));
        textEdit_24->setGeometry(QRect(190, 60, 51, 31));
        label_25 = new QLabel(frame_3);
        label_25->setObjectName(QString::fromUtf8("label_25"));
        label_25->setGeometry(QRect(245, 10, 61, 51));
        label_25->setFont(font1);
        label_25->setAlignment(Qt::AlignCenter);
        label_25->setWordWrap(true);
        textEdit_25 = new QTextEdit(frame_3);
        textEdit_25->setObjectName(QString::fromUtf8("textEdit_25"));
        textEdit_25->setGeometry(QRect(250, 60, 51, 31));
        tabWidget->addTab(data_tab, QString());
        contraint_tab = new QWidget();
        contraint_tab->setObjectName(QString::fromUtf8("contraint_tab"));
        calculate_button = new QPushButton(contraint_tab);
        calculate_button->setObjectName(QString::fromUtf8("calculate_button"));
        calculate_button->setGeometry(QRect(370, 440, 114, 32));
        contraint_table = new QTableWidget(contraint_tab);
        contraint_table->setObjectName(QString::fromUtf8("contraint_table"));
        contraint_table->setGeometry(QRect(10, 10, 831, 411));
        tabWidget->addTab(contraint_tab, QString());
        result_tab = new QWidget();
        result_tab->setObjectName(QString::fromUtf8("result_tab"));
        result_list = new QTableWidget(result_tab);
        result_list->setObjectName(QString::fromUtf8("result_list"));
        result_list->setGeometry(QRect(10, 10, 831, 411));
        objectiveFuntion_label = new QLabel(result_tab);
        objectiveFuntion_label->setObjectName(QString::fromUtf8("objectiveFuntion_label"));
        objectiveFuntion_label->setGeometry(QRect(310, 440, 131, 20));
        objectiveFuntion_label->setAlignment(Qt::AlignCenter);
        objectiveFuntion_label_2 = new QLabel(result_tab);
        objectiveFuntion_label_2->setObjectName(QString::fromUtf8("objectiveFuntion_label_2"));
        objectiveFuntion_label_2->setGeometry(QRect(440, 440, 101, 20));
        objectiveFuntion_label_2->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        tabWidget->addTab(result_tab, QString());
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 915, 22));
        menuFiles = new QMenu(menuBar);
        menuFiles->setObjectName(QString::fromUtf8("menuFiles"));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuFiles->menuAction());
        menuFiles->addAction(actionAdd_Excel_file);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionAdd_Excel_file->setText(QApplication::translate("MainWindow", "Add Excel file", nullptr));
        return_label->setText(QApplication::translate("MainWindow", "Return", nullptr));
        liquidity_label->setText(QApplication::translate("MainWindow", "Liquidity", nullptr));
        cost_label->setText(QApplication::translate("MainWindow", "Cost", nullptr));
        next_button->setText(QApplication::translate("MainWindow", "Next", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "Add", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "Remove", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "Modify", nullptr));
        label->setText(QApplication::translate("MainWindow", "LDD \n"
"Demand Deposit", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "LSD \n"
"Saving Deposit", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "LTD \n"
"Term Deposit", nullptr));
        pushButton_10->setText(QApplication::translate("MainWindow", "Add", nullptr));
        pushButton_11->setText(QApplication::translate("MainWindow", "Remove", nullptr));
        pushButton_12->setText(QApplication::translate("MainWindow", "Modify", nullptr));
        label_10->setText(QApplication::translate("MainWindow", "CLDD \n"
"Demand Deposit", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "CLSD \n"
"Saving Deposit", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "CLTD \n"
"Term Deposit", nullptr));
        label_19->setText(QApplication::translate("MainWindow", "Borrowing\n"
"CLB", nullptr));
        pushButton_19->setText(QApplication::translate("MainWindow", "Add", nullptr));
        pushButton_20->setText(QApplication::translate("MainWindow", "Remove", nullptr));
        pushButton_21->setText(QApplication::translate("MainWindow", "Modify", nullptr));
        label_21->setText(QApplication::translate("MainWindow", "central bank\n"
"RABCB", nullptr));
        label_22->setText(QApplication::translate("MainWindow", "other banks\n"
"RABOB", nullptr));
        label_23->setText(QApplication::translate("MainWindow", "RAGS", nullptr));
        label_24->setText(QApplication::translate("MainWindow", "RADB", nullptr));
        label_25->setText(QApplication::translate("MainWindow", "Advances \n"
"RAA", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(data_tab), QApplication::translate("MainWindow", "Data", nullptr));
        calculate_button->setText(QApplication::translate("MainWindow", "Calculate", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(contraint_tab), QApplication::translate("MainWindow", "Constraints", nullptr));
        objectiveFuntion_label->setText(QApplication::translate("MainWindow", "Objective Function: ", nullptr));
        objectiveFuntion_label_2->setText(QApplication::translate("MainWindow", "Number", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(result_tab), QApplication::translate("MainWindow", "Result", nullptr));
        menuFiles->setTitle(QApplication::translate("MainWindow", "Files", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
