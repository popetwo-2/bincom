def get_ip(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip_address:
        ip = ip_address.split('.')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip