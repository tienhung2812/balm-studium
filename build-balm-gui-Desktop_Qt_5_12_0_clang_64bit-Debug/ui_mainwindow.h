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
#include <QtWidgets/QApplication>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
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
    QWidget *contraint_tab;
    QPushButton *calculate_button;
    QTableWidget *contraint_table;
    QWidget *result_tab;
    QTableWidget *result_list;
    QLabel *objectiveFuntion_label;
    QLabel *objectiveFuntion_label_2;
    QMenuBar *menuBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(859, 559);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setEnabled(true);
        tabWidget->setGeometry(QRect(0, 10, 861, 501));
        data_tab = new QWidget();
        data_tab->setObjectName(QString::fromUtf8("data_tab"));
        return_label = new QLabel(data_tab);
        return_label->setObjectName(QString::fromUtf8("return_label"));
        return_label->setGeometry(QRect(680, 20, 59, 16));
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
        liquidity_list->setGeometry(QRect(20, 40, 256, 391));
        cost_label = new QLabel(data_tab);
        cost_label->setObjectName(QString::fromUtf8("cost_label"));
        cost_label->setGeometry(QRect(400, 20, 59, 16));
        cost_label->setFont(font);
        cost_label->setAlignment(Qt::AlignCenter);
        next_button = new QPushButton(data_tab);
        next_button->setObjectName(QString::fromUtf8("next_button"));
        next_button->setGeometry(QRect(370, 440, 114, 32));
        next_button->setLayoutDirection(Qt::LeftToRight);
        next_button->setAutoFillBackground(false);
        cost_list = new QTableWidget(data_tab);
        cost_list->setObjectName(QString::fromUtf8("cost_list"));
        cost_list->setGeometry(QRect(300, 40, 256, 391));
        return_list = new QTableWidget(data_tab);
        return_list->setObjectName(QString::fromUtf8("return_list"));
        return_list->setGeometry(QRect(580, 40, 256, 391));
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
        menuBar->setGeometry(QRect(0, 0, 859, 22));
        MainWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        return_label->setText(QApplication::translate("MainWindow", "Return", nullptr));
        liquidity_label->setText(QApplication::translate("MainWindow", "Liquidity", nullptr));
        cost_label->setText(QApplication::translate("MainWindow", "Cost", nullptr));
        next_button->setText(QApplication::translate("MainWindow", "Next", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(data_tab), QApplication::translate("MainWindow", "Data", nullptr));
        calculate_button->setText(QApplication::translate("MainWindow", "Calculate", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(contraint_tab), QApplication::translate("MainWindow", "Constraints", nullptr));
        objectiveFuntion_label->setText(QApplication::translate("MainWindow", "Objective Function: ", nullptr));
        objectiveFuntion_label_2->setText(QApplication::translate("MainWindow", "Number", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(result_tab), QApplication::translate("MainWindow", "Result", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
