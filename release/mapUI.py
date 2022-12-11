import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView


class MapView(QWidget):
    def __init__(self, coord, connect):
        super().__init__()
        self.setWindowTitle('Построение миссии полета')
        self.window_width, self.window_height = 1400, 1000
        self.setMinimumSize(self.window_width, self.window_height)
        self.connectToDrone = connect
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.coordinate = coord
        webView = QWebEngineView()
        # print(self.data.getvalue().decode())
        with open("map.html", "r") as f:
            self.html = f.read()
            if connect and not self.coordinate[0] is None and not self.coordinate[1] is None:
                self.changeJS()
            webView.setHtml(self.html)
        layout.addWidget(webView)

    def changeJS(self):
        self.html = self.html.replace("[59.941873, 30.311244]", str(self.coordinate))
        self.html = self.html.replace(" 10,", " 15,")
        isertIndex = self.html.find('$("body")') - 5
        self.html = self.html[
                    : isertIndex] + f"var drone = new L.marker({str(self.coordinate)}, {'{ icon: me }'}).addTo(map);\nmarkerArray = [{'{marker: drone}'}];\n" + self.html[
                                                                                                         isertIndex:]
