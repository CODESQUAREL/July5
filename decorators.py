# def decorator(func):
#     def decorated(input_text):
#         print("함수시작!")
#         func(input_text)
#         print("함수 끝!")
#
#     return decorated
#
#
# @decorator
# def code_square(input_text):
#     print(input_text)
#
# code_square("hello world")
#
# def decorator(func):
#     def decorated(user, width, height):
#         if width > 0 and height > 0:
#             return func(user, width, height)
#         else:
#             raise ValueError("Error")
#
#     return decorated
#
#
# @decorator
# def rect_area(width, height):
#     print(width * height)
#
# @decorator
# def tri_area(width, height):
#     print((width * height)/2)
#
#
# r_area = rect_area(-10, 10)
# print(rect_area)
#
# t_area =
#
#
#
#
#
# #실습 2
# #User 클래스 작성
# #user 클래스 내 is_authenticated 변수 작성
#
# #user객체를 넓이 함수 인자로 전달
#
# #is_authenticated 변수를 확인하고
# #True가 아닐경우 Error를 발생생
#
#
# class User:
#     def __init__(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth=False)
#
# r_area = rect_area(user, 10, 10)
# print(r_area)
#
# t_area = tri_area(user,10, 10)
# print(t_area)
#
#
# #실습3
# #전달되는 모든 인자를 선택적 키워드 인자로 변경