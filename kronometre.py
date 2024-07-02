import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QLCDNumber,
)

from PyQt5.QtCore import QTimer, QTime, Qt


class KronometreUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BATU -  Kronometre")
        self.setGeometry(200, 200, 300, 250)

        self.initUI()

    def initUI(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.zaman_arttir)

        self.zaman = 0
        self.ilk_tur_hizi = None
        self.ikinci_tur_hizi = None
        self.atlet_hizi = None
        self.toplam_hiz = 0

        self.baslangic_saati = ""
        self.bitis_saati = ""
        self.zaman_goster = QLCDNumber()
        self.zaman_goster.setDigitCount(10)  # Salise de dahil olacak şekilde 10 haneli
        self.zaman_goster.display(self.zaman / 10)  # Saliseyi dikkate alarak 10'a böl

        self.baslangic_saati_etiket = QLabel(f"Başlangıç Saati: {self.baslangic_saati}")
        self.bitis_saati_etiket = QLabel(f"Bitiş Saati: {self.bitis_saati}")
        # self.baslangic_saati_etiket.setStyleSheet(
        # "QLabel { color: #FFFFFF; padding-left: 10px; }"
        # )

        self.ig_hiz_yazisi = QLabel("1000 Metre: ")
        self.ig_hiz_goster = QLabel("0")

        self.aim_hiz_yazisi = QLabel("2000 Metre: ")
        self.aim_hiz_goster = QLabel("0")

        self.atlet_hiz_yazisi = QLabel("3000 Metre: ")
        self.atlet_hiz_goster = QLabel("0")

        self.toplam_hiz_yazisi = QLabel("Toplam Hız: ")
        self.toplam_hiz_goster = QLabel("0")

        self.baslat_dugme = QPushButton("Başlat")
        self.baslat_dugme.clicked.connect(self.baslat_kronometre)

        self.durdur_dugme = QPushButton("Durdur")
        self.durdur_dugme.clicked.connect(self.durdur_kronometre)

        self.hiz_dugmesi = QPushButton("Hız Kaydet")
        self.hiz_dugmesi.clicked.connect(self.kaydet_hiz)

        self.sifirla_dugme = QPushButton("Sıfırla")
        self.sifirla_dugme.clicked.connect(self.sifirla_kronometre)

        v_box = QVBoxLayout()

        v_box.addWidget(self.zaman_goster)
        v_box.addWidget(self.baslat_dugme)
        v_box.addWidget(self.durdur_dugme)
        v_box.addWidget(self.hiz_dugmesi)
        v_box.addWidget(self.baslangic_saati_etiket)
        v_box.addWidget(self.ig_hiz_yazisi)
        v_box.addWidget(self.ig_hiz_goster)
        v_box.addWidget(self.aim_hiz_yazisi)
        v_box.addWidget(self.aim_hiz_goster)
        v_box.addWidget(self.atlet_hiz_yazisi)
        v_box.addWidget(self.atlet_hiz_goster)
        v_box.addWidget(self.toplam_hiz_yazisi)
        v_box.addWidget(self.toplam_hiz_goster)
        v_box.addWidget(self.bitis_saati_etiket)
        v_box.addWidget(self.sifirla_dugme)

        self.setLayout(v_box)

    def zaman_arttir(self):
        self.zaman += 1
        self.zaman_goster.display(self.zaman / 10)  # Saliseyi dikkate alarak 10'a böl

    def baslat_kronometre(self):
        self.timer.start(100)  # 0.1 saniyede bir güncelleme yap
        if self.baslangic_saati == "":
            self.baslangic_saati = QTime.currentTime().toString(
                Qt.DefaultLocaleLongDate
            )
            self.baslangic_saati_etiket.setText(
                "Başlangıç Saati: " + str(self.baslangic_saati)
            )

    def durdur_kronometre(self):
        self.timer.stop()

    def kaydet_hiz(self):
        if self.ilk_tur_hizi is None:
            self.ilk_tur_hizi = round(self.zaman / 10, 1)
            self.ig_hiz_goster.setText(str(self.ilk_tur_hizi))
        elif self.ikinci_tur_hizi is None:
            self.ikinci_tur_hizi = round((self.zaman / 10) - self.ilk_tur_hizi, 1)
            self.aim_hiz_goster.setText(str(self.ikinci_tur_hizi))
        elif self.atlet_hizi is None:
            self.atlet_hizi = round(
                (self.zaman / 10) - (self.ikinci_tur_hizi + self.ilk_tur_hizi), 1
            )
            self.atlet_hiz_goster.setText(str(self.atlet_hizi))
            # elif self.toplam_hiz == 0:
            self.toplam_hiz = round(
                self.ilk_tur_hizi + self.ikinci_tur_hizi + self.atlet_hizi, 1
            )
            self.toplam_hiz_goster.setText(str(self.toplam_hiz))

            if self.bitis_saati == "":
                self.bitis_saati = QTime.currentTime().toString(
                    Qt.DefaultLocaleLongDate
                )
                self.bitis_saati_etiket.setText("Bitiş Saati: " + str(self.bitis_saati))

    def sifirla_kronometre(self):
        self.zaman = 0
        self.ilk_tur_hizi = None
        self.ikinci_tur_hizi = None
        self.atlet_hizi = None
        self.toplam_hiz = 0
        self.baslangic_saati = ""
        self.bitis_saati =""
        self.zaman_goster.display(self.zaman / 10)
        self.ig_hiz_goster.setText("0")
        self.aim_hiz_goster.setText("0")
        self.toplam_hiz_goster.setText("0")
        self.atlet_hiz_goster.setText("0")
        self.baslangic_saati_etiket.setText("Başlangıç Saati:")
        self.bitis_saati_etiket.setText("Bitiş Saati:")


css_style = """

/* Genel stil kuralları */
* {
  background-color: #333333; /* Mavi arka plan */
  color: #FFFFFF; /* Beyaz yazı */
}
QLCDNumber {
    background-color: #333333; /* Arka plan rengi */
    color: #FFFFFF; /* Yazı rengi */
    border: 2px solid #CCCCCC; /* Kenarlık rengi ve kalınlığı */
    border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
    padding: 2px; /* İçerik dolgusu */
    color: #ffffff; /* Yazı rengi beyaz */
    font-family: Arial; /* Yazı tipi Arial */
    font-size: 14pt; /* Yazı boyutu 14 pt */
    font-weight: bold; /* Kalın yazı tipi */
    width: 70px; /* Genişlik */
    height: 51px; /* Yükseklik */
    border: none; /* Kenarlık yok */
}
/* Butonların stil kuralları */
QLabel {
  background-color: #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi beyaz */
  font-family: Arial; /* Yazı tipi Arial */
  font-size: 14pt; /* Yazı boyutu 14 pt */
  font-weight: bold; /* Kalın yazı tipi */
  width: 70px; /* Genişlik */
  height: 51px; /* Yükseklik */
  border: none; /* Kenarlık yok */
}
QLabel {text-align: center;}
QLineEdit {
  background-color: #ffffff; /* Başlangıçta arka plan rengi beyaz */
}

QLineEdit:!enabled {
  background-color: #ffff00; /* İçeriği dolu olan QLineEdit'in arka plan rengi sarı */
}
/* QLineEdit stil kuralları */
QLineEdit {
  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  /*padding: 6px; /* İçerik dolgusu */
  background-color: #ffffff; /* Arka plan rengi */
  color: #333333; /* Yazı rengi */
}

/* QLineEdit hover efekti */
QLineEdit:hover {
  border-color: #3498db; /* Kenarlık rengi */
}

/* QLineEdit odaklandığında */
QLineEdit:focus {
  border-color: #3498db; /* Kenarlık rengi */
}

/* LineEdit stil kuralları */
QLineEdit {
  border: 1px solid #ccc; /* Kenarlık rengi ve kalınlığı */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  background-color: #ffffff; /* Arka plan rengi */
}

/* LineEdit üzerine gelindiğinde */
QLineEdit:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
}


/* Butonların stil kuralları */
QPushButton, QToolButton {
  background-color:  #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi beyaz */
  border: 1px solid #b3ff26; /* Kenarlık */
  border-radius: 4px; /* Kenarlık köşeleri yuvarlatma */
  padding: 8px 16px; /* Buton içeriği için dolgular */
  font: 22px;


}

/* Buton hover efekti */
QPushButton:hover, QToolButton:hover {
  background-color: #2980b9; /* Hover rengi */
  border-color: #2980b9; /* Kenarlık rengi */
}

/* Buton basılma efekti */
QPushButton:pressed, QToolButton:pressed {
  background-color: #1f618d; /* Basılma rengi */
  border-color: #1f618d; /* Kenarlık rengi */
}


/* GroupBox stil kuralları */
QGroupBox {
  border: 2px solid grey;/*#ccc;*/ /* Kenarlık rengi ve kalınlığı */
  border-radius: 6px; /* Kenarlık köşeleri yuvarlatma */
  padding: 6px; /* İçerik dolgusu */
  background-color: #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi */
}

/* GroupBox üzerine gelindiğinde */
QGroupBox:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
color:#ffffff /* Yazı rengi */
}

/* CheckButton ve RadioButton stil kuralları */
QCheckBox, QRadioButton {
  color: #ffffff; /* Yazı rengi */
}

/* CheckButton ve RadioButton üzerine gelindiğinde */
QCheckBox:hover, QRadioButton:hover {
  background-color: #ffff00; /* Sarı arka plan rengi */
  color: black; /* Yazı rengi */
  border-radius: 3px; /* Kenarlık köşeleri yuvarlatma */
  /*padding: 1px; /* İçerik dolgusu */
}

/*--------------------------------------------------------------------*/

/* StackedWidget ileri ve geri butonlarının stil kuralları */
QStackedWidget &gt; QAbstractButton {
  background-color: #333333; /* Arka plan rengi ile aynı renk */
  border: none; /* Kenarlık yok */
  width: 0; /* Genişlik sıfır */
  height: 0; /* Yükseklik sıfır */
}

/* İleri ve geri butonlarının üzerine gelindiğinde */
QStackedWidget &gt; QAbstractButton:hover {
  background-color: #333333; /* Arka plan rengi ile aynı renk */
}

/* Butonların stil kuralları */
QPushButton {
  background-color: #333333; /* Arka plan rengi */
  color: #ffffff; /* Yazı rengi beyaz */
  font-family: Arial; /* Yazı tipi Arial */
  font-size: 14pt; /* Yazı boyutu 14 pt */
  font-weight: bold; /* Kalın yazı tipi */
  width: 70px; /* Genişlik */
  height: 51px; /* Yükseklik */
  border: none; /* Kenarlık yok */
}

/* Buton hover efekti */
QPushButton:hover {
  background-color: #2980b9; /* Hover rengi */
}

"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uygulama = KronometreUygulamasi()
    uygulama.resize(300, 500)
    app.setStyleSheet(css_style)  # CSS stilini uygula
    uygulama.show()
    sys.exit(app.exec_())
