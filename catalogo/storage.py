from django.core.files.storage import Storage
from django.conf import settings
import cloudinary
import cloudinary.uploader


class CloudinaryStorage(Storage):
    def __init__(self, option=None):
        if not option:
            option = settings.CLOUDINARY_STORAGE
        
        # Configurar Cloudinary
        cloudinary.config(
            cloud_name=option['CLOUD_NAME'],
            api_key=option['API_KEY'],
            api_secret=option['API_SECRET'],
            secure=True
        )

    def _open(self, name, mode='rb'):
        return None

    def _save(self, name, content):
        # Subir a Cloudinary
        result = cloudinary.uploader.upload(content, public_id=name)
        return result['public_id']

    def exists(self, name):
        return False

    def url(self, name):
        # Generar URL de Cloudinary
        result = cloudinary.CloudinaryImage(name).build_url()
        return result

    def size(self, name):
        return 0

    def delete(self, name):
        try:
            cloudinary.uploader.destroy(name)
        except:
            pass