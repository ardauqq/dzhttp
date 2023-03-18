import requests

TOKEN = ''


class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.yandex_url = 'https://cloud-api.yandex.net/'

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.yandex_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    a = YandexDisk(token=TOKEN)
    a.upload_file_to_disk('netology/Bible2.txt', 'Bible_txt.txt')
