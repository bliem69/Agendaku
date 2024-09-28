import PySimpleGUI as pg
import os

import fungsiAgenda

if os.path.exists('agenda.txt'):
    agendaku = fungsiAgenda.openFile()
else:
    fungsiAgenda.createAgenda()
    agendaku = fungsiAgenda.openFile()


#Element
labelInput = pg.Text("Masukkan Agenda: ")
labelDaftar = pg.Text("Daftar Agenda: ")
boxInput = pg.InputText(key="keyBoxInput", size=(40,1))
tombolTambah = pg.Button("Tambah", key="keyTambah")
tombolHapus = pg.Button("Hapus", key="keyHapus")
tombolKeluar = pg.Button("Exit", key="keyKeluar")
daftarAgenda = pg.Listbox(values=agendaku, key="keyDaftarAgenda", size=(60, 10))

#Window

window = pg.Window("Daftar Agendaku",
                   layout=[[labelInput], [boxInput, tombolTambah, tombolHapus, tombolKeluar],
                           [labelDaftar], [daftarAgenda]],
                   size=(1000, 600),
                   font=("Helvetica", 20))

while True:
    event, data = window.read()
    print(event)
    print(data)

    match event:
        case "keyTambah":
            #menambahkan agenda
            agendaBaru = data["keyBoxInput"]
            agendaku.append(agendaBaru + '\n')
            window["keyDaftarAgenda"].update(values=agendaku)
        case "keyHapus":
            #menghapus agenda
            agendaHapus = data["keyDaftarAgenda"][0]
            agendaku.remove(agendaHapus)
            window["keyDaftarAgenda"].update(values=agendaku)
        case "keyKeluar":
            #keluar
            fungsiAgenda.saveAgenda(agendaku=agendaku)
            break
        case pg.WINDOW_CLOSED:
            fungsiAgenda.saveAgenda(agendaku=agendaku)
            break

window.close()

