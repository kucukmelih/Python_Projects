import os  
import sys 
import tty  # Terminalin giriş modunu değiştirmek için kullanılan kütüphane
import termios  # Terminalin giriş/çıkış ayarlarını değiştirmek için kullanılan kütüphane

# Dosya okuma sınıfı
class FileReader:
    def __init__(self, file_path): 
        self.file_path = file_path  
        self.content = self.read_file()  # Dosyanın içeriğini okuyup saklıyoruz

    # Dosya okuma fonksiyonu
    def read_file(self):
        if not os.path.exists(self.file_path):
            print(f"Error: The file '{self.file_path}' does not exist.")
            sys.exit(1)
        try:
            # Dosyayı okuyoruz ve satır satır listeye ekliyoruz
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

# Sayfalama işlemi 
class Pagination:
    def __init__(self, content, page_size):
        # İçeriği, her biri page_size kadar satırdan oluşan sayfalara bölüyoruz
        self.pages = [content[i:i + page_size] for i in range(0, len(content), page_size)]

    # Belirtilen sayfa numarasını döndüren fonksiyon
    def get_page(self, page_number):
        # Eğer sayfa numarası geçerli ise, sayfayı döndürüyoruz, değilse None döndürür
        return self.pages[page_number] if 0 <= page_number < len(self.pages) else None

# Terminal işlemleri için 
class TerminalManager:
    @staticmethod
    def display_page(content, current_page, total_pages, total_lines, show_footer=True):
        # Terminali temizliyoruz (Windows için 'cls', diğer sistemler için 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        # Sayfanın içeriğini ekrana yazdırıyoruz
        print(''.join(content))
        # Eğer footer (sayfa bilgisi) gösterilecekse
        if show_footer:
            print(f"\nSayfa {current_page + 1}/{total_pages}, Toplam Satır: {total_lines}")
            print("Devam için 'Boşluk', önceki sayfa için 'B', çıkmak için 'Q'.")

# Kullanıcıdan klavye girdisi almak 
class InputHandler:
    @staticmethod
    def wait_for_input():
        # Terminal ayarlarını değiştirmek için dosya tanımlayıcısını alıyoruz
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Terminali ham (raw) moda getiriyoruz, böylece girdileri satır sonu olmadan okuyabiliriz
            tty.setraw(fd)
            while True:
                # Klavyeden bir karakter okuyoruz ve büyük harfe çeviriyoruz
                char = sys.stdin.read(1).upper()
                # Eğer karakter ' ', 'Q' veya 'B' ise bu karakteri geri döndürüyoruz
                if char in [' ', 'Q', 'B']:
                    return char
        finally:
            # Terminali eski ayarlarına geri döndürüyoruz
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def main():
    if len(sys.argv) != 2:
        print("Kullanım: python text_browser.py <dosya_yolu>")
        sys.exit(1)

    # FileReader sınıfını kullanarak dosya içeriğini okuyoruz
    file_reader = FileReader(sys.argv[1])
    content = file_reader.content  # İçeriği alıyoruz
    total_lines = len(content)  # Toplam satır sayısını hesaplıyoruz

    # Pagination sınıfını kullanarak içeriği sayfalara bölüyoruz (her sayfada 10 satır)
    pagination = Pagination(content, page_size=10)
    total_pages = len(pagination.pages)  # Toplam sayfa sayısını hesaplıyoruz
    current_page = 0  # Başlangıç sayfası (ilk sayfa)

    # Sonsuz döngüyle sayfalar arasında gezinmeyi sağlıyoruz
    while True:
        # Mevcut sayfayı alıyoruz
        page_content = pagination.get_page(current_page)
        # Eğer sayfa yoksa, döngüyü sonlandırıyoruz
        if page_content is None:
            break

        # Sayfayı terminale yazdırıyoruz
        TerminalManager.display_page(page_content, current_page, total_pages, total_lines)
        # Kullanıcıdan giriş bekliyoruz (boşluk, 'B', 'Q')
        user_input = InputHandler.wait_for_input()

        if user_input == 'Q':
            # Çıkmadan önce sayfayı footer olmadan tekrar gösteriyoruz
            TerminalManager.display_page(page_content, current_page, total_pages, total_lines, show_footer=False)
            break
        # Eğer kullanıcı 'boşluk' tuşuna basmışsa bir sonraki sayfaya geçiyoruz
        elif user_input == ' ':
            current_page = min(current_page + 1, total_pages - 1)  # Sayfa sınırını aşmıyoruz
        # Eğer kullanıcı 'B' tuşuna basmışsa bir önceki sayfaya dönüyoruz
        elif user_input == 'B':
            current_page = max(current_page - 1, 0)  # İlk sayfanın altına inmiyoruz

    # Programdan çıkıyoruz
    print("Metin tarayıcıdan çıkılıyor...\n")

if __name__ == "__main__":
    main()
