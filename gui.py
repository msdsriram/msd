from PyQt5.QtWidgets import QMessageBox

reply = QMessageBox.question(None, "Quick Question", "Do you like using QGIS?",
                             QMessageBox.Yes | QMessageBox.No)

if reply == QMessageBox.Yes:
    QMessageBox.information(None, "Nice!", "Glad you enjoy it!")
else:
    QMessageBox.information(None, "Oh no!", "Hope it grows on you!")