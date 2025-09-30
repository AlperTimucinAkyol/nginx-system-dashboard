# Nginx System Dashboard

Gerçek zamanlı sistem izleme panosu:  
- Nginx → statik HTML + API proxy  
- Python + `psutil` → CPU, RAM, Disk verisi  
- Tarayıcıda canlı güncellenen dashboard

## Kurulum

```bash
# 1. Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# 2. Bağımlılıkları yükle
pip install -r requirements.txt

# 3. API'yi başlat
python api/sysapi.py

# 4. Nginx'i başlat (kendi dizininde)
nginx -c nginx/conf/nginx.conf

Kullanım
Dashboard: http://localhost:8081
API: http://localhost:8081/api/sysinfo