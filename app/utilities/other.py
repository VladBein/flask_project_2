from typing import Any
import hmac
from hashlib import sha256
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64


#Шифрование данных:
class HashingData:
	"""Хеширование данных"""

	__key: str
	__salt: str

	def __init__(self):
		self.__key = "qwerty123"
		self.__salt = "123123"

	def calculate_hash(self, string: Any) -> str:
		"""Вычисляет хэш по алгоритму SHA256."""
		salted_string = str(string) + self.__salt
		return hmac.new(
			self.__key.encode(),
			msg=salted_string.encode(),
			digestmod=sha256
		).hexdigest().upper()


def encrypts_data(data: str) -> str:
	"""Зашифровывает данные стандартом base64."""
	return base64.b64encode(data.encode()).decode()

def decrypts_data(data: str) -> str:
	"""Расшифровывает данные, зашифрованные стандартом base64."""
	try:
		return base64.b64decode(data.encode() + b'===').decode()
	except (UnicodeDecodeError, Exception):
		return ""


#Обработка данных:


#Логгирование:
def records_log_user_registration(user_id: int) -> None:
	"""Записывает лог регистрации пользователя."""
	logging.getLogger('app_logger').info(f"REG user_id = {user_id}")

def records_log_user_restorer(user_id: int) -> None:
	"""Записывает лог восстановления пользователя."""
	logging.getLogger('app_logger').info(f"RESTORE user_id = {user_id}")

def records_log_user_authentication(user_id: int, type_auth: str) -> None:
	"""Записывает лог аутентификации пользователя."""
	logging.getLogger('app_logger').info(f"user_id = {user_id} по {type_auth}")

def records_log_change_password(user_id: int) -> None:
	"""Записывает лог изменения пароля."""
	logging.getLogger('app_logger').info(f"CHANGE_PASSWORD user_id = {user_id}")


#Отправка сообщений по эл. почте:
class Email:
	"""Электронная почта"""

	__email: str
	__password: str

	def __init__(self):
		self.__email = '***@***.**'
		self.__password = '***********'

	def send(self, to: str, subject: str, text: str) -> None:
		"""Отправляет электронное письмо."""
		pass
		#msg = MIMEMultipart()
		#msg['To'] = to
		#msg['From'] = self.__email
		#msg['Subject'] = subject
		#msg.attach(MIMEText(text_message, 'plain'))
		#server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
		#server.login(self.__email, self.__password)
		#server.send_message(msg)
		#server.quit()
