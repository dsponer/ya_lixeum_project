from PyQt5.QtWidgets import QPushButton, QLabel, QCalendarWidget, QToolButton, QRadioButton, QCheckBox,\
    QTableView, QColumnView, QListWidget, QTreeWidget, QTableWidget, QComboBox, QFontComboBox, QLineEdit, QTextEdit,\
    QDateEdit, QDateTimeEdit, QScrollBar, QSlider, QKeySequenceEdit, QTextBrowser, QGraphicsView, QLCDNumber,\
    QProgressBar, QFrame, QOpenGLWidget, QPlainTextEdit, QDoubleSpinBox, QTimeEdit, QCommandLinkButton,\
    QDialogButtonBox, QListView, QTreeView, QDial, QSpinBox


class SpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(QSpinBox, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class Dial(QDial):
    def __init__(self, parent=None):
        super(QDial, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class OpenGLWidget(QOpenGLWidget):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class Frame(QFrame):
    def __init__(self, parent=None):
        super(Frame, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class ProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super(QProgressBar, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class LCDNumber(QLCDNumber):
    def __init__(self, parent=None):
        super(QLCDNumber, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class GraphicsView(QGraphicsView):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TextBrowser(QTextBrowser):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class KeySequenceEdit(QKeySequenceEdit):
    def __init__(self, parent=None):
        super(QKeySequenceEdit, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class Slider(QSlider):
    def __init__(self, parent=None):
        super(QSlider, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class ScrollBar(QScrollBar):
    def __init__(self, parent=None):
        super(QScrollBar, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class DateTimeEdit(QDateTimeEdit):
    def __init__(self, parent=None):
        super(QDateTimeEdit, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class DateEdit(QDateEdit):
    def __init__(self, parent=None):
        super(QDateEdit, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class TimeEdit(QTimeEdit):
    def __init__(self, parent=None):
        super(QTimeEdit, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class DoubleSpinBox(QDoubleSpinBox):
    def __init__(self, parent=None):
        super(QDoubleSpinBox, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class PlainTextEdit(QPlainTextEdit):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TextEdit(QTextEdit):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class LineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(QLineEdit, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class FontComboBox(QFontComboBox):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class ComboBox(QComboBox):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2),  event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TreeWidget(QTreeWidget):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class ListWidget(QListWidget):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class ColumnView(QColumnView):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TableView(QTableView):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class TreeView(QTreeView):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class ListView(QListView):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)


class ToolButton(QToolButton):
    def __init__(self, parent=None):
        super(ToolButton, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class RadioButton(QRadioButton):
    def __init__(self, parent=None):
        super(RadioButton, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class CheckBox(QCheckBox):
    def __init__(self, parent=None):
        super(QCheckBox, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class CommandLinkButton(QCommandLinkButton):
    def __init__(self, parent=None):
        super(QCommandLinkButton, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class DialogButtonBox(QDialogButtonBox):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 20)
        self.setMouseTracking(False)


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super(PushButton, self).__init__(parent)

    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class Label(QLabel):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - (self.height() / 2))
        self.setMouseTracking(False)


class CalendarWidget(QCalendarWidget):
    def mousePressEvent(self, event):
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.move(event.windowPos().x() - (self.width() / 2), event.windowPos().y() - 30)
        self.setMouseTracking(False)
