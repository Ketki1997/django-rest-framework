import jwt
from django.contrib.auth.models import AnonymousUser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken
from .models import Student

# def current_user_middleware(view_func):
#     def _wrapped_view(request, *args, **kwargs):
#         print("Middleware is executing!")
#         try:
#             authorization_header = request.headers.get('Authorization', None)

#             if not authorization_header:
#                 return view_func(request, *args, **kwargs)
            
#             token = authorization_header.split('Bearer ')[1]
#             print(token, '-----token-----------------')
#             # Assuming you are using a simple JWT token without encryption
#             # If you are using encrypted tokens, adjust this part accordingly
#             try:
#                 decoded_token = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
#                 print(decoded_token, '---------decoded_token--------------')
#                 access_token = AccessToken(decoded_token['access'])
#     # Rest of the code
#             except Exception as e:
#                 print(f"Error during token decoding: {e}")
#             # Set the user in the request
#             request.user = access_token.user

#             # Check if the user exists
#             user = Student.objects.filter(
#                 id=request.user.id,
#                 is_deleted=False,
#                 is_active=True,
#                 user_type=request.user.user_type
#             ).first()

#             if not user:
#                 return JsonResponse({'error': 'Not Authorized'}, status=401)

#             return view_func(request, *args, **kwargs)

#         except jwt.ExpiredSignatureError:
#             return JsonResponse({'error': 'Token has expired'}, status=401)
#         except jwt.InvalidTokenError:
#             return JsonResponse({'error': 'Invalid token'}, status=401)
#         except Exception as e:
#             return JsonResponse({'error': 'Not Authorized'}, status=401)

#     return _wrapped_view

def current_user_middleware(get_response):
    def middleware(request):
        print("Middleware is executing!")

        authorization_header = request.headers.get('Authorization', None)

        if not authorization_header or not authorization_header.startswith('Bearer '):
            return JsonResponse({'error': 'Authorization token is missing or invalid'}, status=401)

        try:
            # Extract the token part without the "Bearer" prefix
            token = authorization_header.split('Bearer ')[1]
            print(token, '-----token-----------------')

            try:
                access_token = AccessToken(token)
                user_id = access_token.payload['user_id']
                # username = access_token.payload['username']
                print(access_token,"qwertyuiowertyui")
            except Exception as e:
                return JsonResponse({'error': 'Token is invalid or expired'}, status=401)


            request.user = {
                'id': user_id,
                # 'username': username,
            }
            print(request.user,"-----------request.user---------------")

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'error': f'Error: {e}'}, status=401)

        return get_response(request)

    return middleware
