class FileIOMixin:
    """
    Миксин для работы с файлами
    """

    def to_file(self, filename: str) -> None:
        """
        Сохраняет строковое представление объекта в файл

        :param filename: путь к файлу
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(self))
