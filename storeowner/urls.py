from django.urls import path
from storeowner import views

urlpatterns=[
    path('', views.stores, name='stores'),
    path('books_list', views.books_list, name='books_list'),
    path('login_seller', views.login_seller, name='login_seller'),
    path('register_seller', views.register_seller, name='register_seller'),
    path('logout_seller', views.logout_seller, name='logout_seller'),
    path('storeform', views.storeform, name='storeform'),
    path('book_library<str:storename>', views.book_library, name='book_library'),
    path('bookform<str:storename>', views.bookform, name='bookform'),
    path('book_update<str:bookid>', views.book_update, name='book_update'),
    path('book_delete<str:bookid>', views.book_delete, name='book_delete'),
    
]