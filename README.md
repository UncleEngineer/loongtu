# Loong Tu Library (loongtu)

Youtube: https://youtu.be/RefHYXqFrUI

สวัสดีจร้าาาา นี่ลุงวิศวกรเอง ไลบรารี่นี้ใช้สำหรับฝึกสร้างไลบรารี่เป็นของตัวเอง ความสามารถคือ

  - แสดงชื่อลุงตู่ภาษาอังกฤษ 
  - แสดงชื่อลุงตู่ภาษาไทย


### วิธีติดตั้งแสนง่าย

ไปกดไลค์เพจลุงก่อนเลย เสริมเกราะป้องกัน 555 [ลุงวิศวกร สอนคำนวณ](https://www.facebook.com/UncleEngineer)  ฮ่าาา ไม่บังคับ (กดไลค์เพจลุงหน่อยๆ 555)

เราจะติดตั้งผ่านเจ้า pip

```sh
pip install loongtu
```

ง่ายไหมล่ะ

วิธีใช้ก็ง่ายมาก
- เปิด Python แล้วพิพม์ตามนี้เลย

```sh
from loongtu import Loongtu

myloong = Loongtu()
print(myloong)
print(myloong.name)
print(myloong.lastname)
print(myloong.nickname)
myloong.WhoIAm()
print(myloong.email)
myloong.thainame()
print('--------')
mypaa = Loongtu()
mypaa.name = 'Somsri'
mypaa.lastname = 'Konthai'
mypaa.nickname = 'Sri'
mypaa.WhoIAm()
print(mypaa.name)
print(mypaa.lastname)
print(mypaa.nickname)
```

### Visit

แวะเข้าไปเยี่ยมชมกันได้ แหล่งกบดานเรามีสอนหลายวิชา

| เนื้อหา | ลิ้งค์ |
| ------ | ------ |
| ลุงมีวิชาอะไรบ้าง |http://uncle-engineer.com/ |
| อ่านบทความใน Medium  | https://medium.com/@UncleEngineer |
| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer |
| ------ | ------ |
| สร้างไฟล์ README  | https://dillinger.io/ |

### ติดตามตอนต่อไป...ในเพจ "ลุงวิศวกร สอนคำนวณ"
