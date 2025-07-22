# 📚 Kitap Yönetim Sistemi

Bu proje, kullanıcıların kitap bilgilerini (başlık, yazar, yıl) girebildiği, güncelleyebildiği ve silebildiği basit bir kitap yönetim sistemidir. Proje FastAPI (backend) ve basit HTML/CSS/JS (frontend) ile geliştirilmiştir.

## 🚀 Özellikler

- 📖 Kitap ekleme
- 📝 Kitap bilgilerini düzenleme
- ❌ Kitap silme
- 💾 JSON dosyasında veri saklama

## 🗂️ Proje Yapısı

books_system_project/
├── backend/
│ ├── main_book.py # FastAPI backend uygulaması
│ ├── database.json # Kitap verilerinin saklandığı dosya
├── frontend/
│ ├── index.html # Ana HTML arayüzü
│ ├── script.js # JavaScript ile API bağlantısı
│ ├── style.css # Sayfa tasarımı
├── env/ # Python sanal ortamı (opsiyonel)



## 🔧 Kurulum ve Çalıştırma

1. **Sanal Ortam Oluştur (Opsiyonel)**  
python -m venv env
.\env\Scripts\activate



2. **Gerekli Kütüphaneleri Yükle**  
pip install fastapi uvicorn



3. **Backend’i Başlat**  
cd backend
uvicorn backend.main_book:app --reload


4. **Frontend’i Aç**  
`frontend/index.html` dosyasını çift tıklayarak tarayıcınızda açın.

## 📷 Arayüz Görüntüsü

Ana sayfa üzerinden kitap bilgilerini girebilir, listeleyebilir ve düzenleyebilirsiniz:

![Kitap Sistemi](frontend_preview.png)

## 📌 Not

- Bu proje sadece eğitim ve pratik amaçlıdır.
- API endpointleri `/books` üzerinden çalışır.

## 🪪 Lisans

Açık kaynak ve ücretsizdir.
