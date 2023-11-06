import cv2
import zxingcpp

# noinspection PyArgumentList
def barcodeOku():
	_isbn=""
	img = cv2.imread('bc2.jpg')
	results = zxingcpp.read_barcodes(img)
	for result in results:
		_isbn=format(result.text)
	if len(results) == 0:
		print("Could not find any barcode.")
	return _isbn

"""def barcodeYakala():
	kamera = cv2.VideoCapture(0)
	while True:
		ret, goruntu = kamera.read()
		cv2.imshow("Kamera", goruntu)
		# "s" tuşuna basıldığında anlık görüntüyü kaydet
		if cv2.waitKey(1) & 0xFF == ord('s'):
			cv2.imwrite("bc2.jpg", goruntu)
			#print("Anlık görüntü kaydedildi.")
			break
		# "q" tuşuna basıldığında döngüyü kır ve pencereyi kapat
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	kamera.release()
	cv2.destroyAllWindows()"""


def barcodeYakala():
	kamera_numarasi = 0  # Başlangıçta ön kamerayı kullanın (kamera numarası 0 veya 1 olabilir)
	kamera = cv2.VideoCapture(kamera_numarasi)

	if not kamera.isOpened():
		#print("Arka kamera bulunamadı. Ön kamera kullanılıyor...")
		kamera_numarasi = 1  # Ön kamerayı kullanın
		kamera = cv2.VideoCapture(kamera_numarasi)

	while True:
		ret, goruntu = kamera.read()
		cv2.imshow("Kamera", goruntu)

		if cv2.waitKey(1) & 0xFF == ord('s'):
			cv2.imwrite("bc2.jpg", goruntu)
			break

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	kamera.release()
	cv2.destroyAllWindows()
