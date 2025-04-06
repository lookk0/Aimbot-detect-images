import os

paths = "bot.png"  # เปลี่ยนเป็นชื่อไฟล์ที่ต้องใช้

if os.path.exists(paths):
    print("✅ ไฟล์ภาพมีอยู่จริง")
else:
    print("❌ ไม่พบไฟล์! ตรวจสอบชื่อไฟล์และตำแหน่งอีกครั้ง")
