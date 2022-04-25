import os

class LoadCsvFile:
    def __init__(self, i_o, bookmark_service):
        """Initializes command with IO and BookmarkService object.

        Args:
            i_o (class, optional):
                Object providing IO methods (read() and write()).
            bookmark_service (class, optional):
                Service class containing business logic.
        """
        self._io = i_o
        self._bookmark_service = bookmark_service

    def __str__(self):
        return "lataa csv -tiedosto"

    def execute(self):
        """Executes command."""

        self._io.write(
                "Ladataan vinkit csv-tiedostosta, syötä:""\n"
                "tiedoston hakemiston absoluutinen polku tai""\n"
                "x, jos haluat palata valikkoon tai""\n"
                "enter, jos tiedosto sijaitsee sovelluksen kansiossa csv_files""\n"
                )

        self._io.write(
                "Nykyisen työkansion polku: " + str(os.getcwd())
                )

        user_input = self._io.read("csv-tiedoston hakemiston polku: ").strip()

        if user_input  == "x":
            return

        if user_input  == "":
            self._bookmark_service.create_default_csv_directory_if_missing()
            dir_path = self._bookmark_service.create_default_directory_path()
        elif user_input :
            dir_path = self._bookmark_service.correct_dir_path(user_input )

        if not self._bookmark_service.exists(dir_path):
            self._io.write("\n""polkua ei löytynyt")
            return

        user_input  = self._io.read("csv-tiedoston nimi: ").strip()
        if user_input  == "x":
            return

        if user_input :
            filename = self._bookmark_service.correct_filename(user_input )
            file_path = os.path.join(dir_path, filename)

            if not self._bookmark_service.exists(file_path):
                self._io.write("\n""tiedostoa ei löytynyt")
                return

            load = self._bookmark_service.load_file(file_path)
            if load:
                self._io.write("\n""kirjanmerkit ladattiin tiedostosta ""\n" +file_path)
            else:
                self._io.write("\n""tiedosto on virheellinen")
