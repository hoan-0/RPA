import qrcode
# 학번, 이름, 전공 정보를 입력 받아 그 정보에 대한 QR코드 만들기
name = input("이름을 입력하시오: ")
num = input("학번을 입력하시오: ")
major = input("전공을 입력하시오: ")


qr_data = (f"이름: {name}, 학번: {num} 전공:{major}")
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)