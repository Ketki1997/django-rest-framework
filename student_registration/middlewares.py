import jwt
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken

def current_user_middleware(get_response):
    def middleware(request, *args, **kwargs):
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

        return get_response(request, *args, **kwargs)

    return middleware
