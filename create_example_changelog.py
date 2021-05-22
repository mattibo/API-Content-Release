# create example changelog file (markdown format)

from mdutils.mdutils import MdUtils

chlog_file = MdUtils(file_name="CHANGELOG.example.md")

chlog_file.new_header(level=1, title='KW x')
chlog_file.new_header(level=2, title="Service")
chlog_file.new_header(level=3, title="Hinzugefügt")

services_added = ["ABD", "DEF"]

chlog_file.new_list(services_added)

chlog_file.new_header(level=3, title="Gelöscht")
services_removed = ["XYZ"]
chlog_file.new_list(services_removed)

chlog_file.new_header(level=3, title="Modifiziert")
services_modified = ["Service-ID", "Attribut", "Alter Wert", "Neuer Wert"]
services_modified.extend(["1", "name", "ABC", "DEF"])
chlog_file.new_table(columns=4, rows=2, text=services_modified, text_align="left")

chlog_file.create_md_file()

