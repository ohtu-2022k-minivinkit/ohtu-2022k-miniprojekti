import os
class CreateCsvFile:
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
        self._change_filename = False

    def __str__(self):
        return "muodosta csv -tiedosto"

    def execute(self):
        """Executes command."""
        filename = self._bookmark_service.create_default_filename()

        if self._change_filename:
            new_filename = self._io.read("kirjoita tiedostolle uusi nimi: ").strip()

        else:
            self._io.write(
                "Muodostetaan vinkeistä csv -tiedosto\n(x takaisin valikkoon)"
                )

            self._io.write(
                "Voit käyttää oletuksia ja ohittaa kysymykset enterillä\n"
                )

            new_filename = self._io.read("tiedostonimi: ").strip()

        if new_filename == "x":
            self._change_filename = False
            return

        self._io.write(
                "\n" + "Nykyisen työkansion polku: " + str(os.getcwd())
                )

        new_dir_path = self._io.read(
            "sijoituskansion absoluuttinen polku: "
            ).strip()

        if new_dir_path:
            new_dir_path = self._bookmark_service.correct_dir_path(new_dir_path)
            if not self._bookmark_service.exists(new_dir_path):
                new_dir_path = None
                self._io.write(
                    "\npolkua ei löytynyt, tiedosto sijoitetaan sovelluksen kansioon"
                    )

        if new_filename:
            filename = self._bookmark_service.correct_filename(new_filename)

            if new_dir_path:
                file_path = new_dir_path + filename
            else:
                file_path = self._bookmark_service.create_default_filepath(filename)

            if self._bookmark_service.exists(file_path):
                overwrite_answer = self._io.read(
                    "Tiedosto on jo olemassa, ylikirjoitetaanko tiedosto (k/e)? "
                    )

                if overwrite_answer != "k":
                    self._io.write("\ntiedostoa ei ylikirjoitettu")
                    self._change_filename = True
                    self.execute()
                    return

        if new_dir_path:
            file_path = new_dir_path + filename
        else:
            file_path = self._bookmark_service.create_default_filepath(filename)

        self._bookmark_service.create_file(file_path)

        file_info = 'antamaasi kansioon' if new_dir_path else 'sovelluksen csv_files -kansioon,'
        self._io.write(f"\nTiedosto {filename} on tallennettu {file_info}")
        self._io.write(f"polku tiedostoon: {file_path}")
        self._change_filename = False
