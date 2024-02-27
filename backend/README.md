Activare mediu virtual python:
 - .\venv\Scripts\activate

Go to the project directory:
 - cd .\backend\

Activare server django:
 - python manage.py runserver
 - python manage.py runserver 0.0.0.0:80    //pentru rulare publica

Acces proiect:
 -  http://127.0.0.1:8000/


Creare aplicatie:
 - python manage.py startapp <app_name>

 python manage.py makemigrations products
 python manage.py sqlmigrate products 0001
 python manage.py migrate

Task-uri realizate:
 - Doar utilizatorii logati au acces la detaliile produselor
 - Am adugat mai multe detalii pentru un produs
 - Am adaugat cautarea de produse noi
 - chat global si temporar https://www.geeksforgeeks.org/realtime-chat-app-using-django/
 - coprimarea login, logout, register intr-un modul separat
 - crearea unui meniu pentru navigare
 - adaugarea de elemente statice + style bootstrap
 - css pentru chat https://mdbootstrap.com/docs/standard/extended/chat/
 - de mutat styleurile pt chat
 - de afisat dreapta stanga in chat

De realizat:
 - Eroare: cand sunt pe pagina de produse, nu pot sa dau click pe toate linkurile din meniu 
 - pagina de produse sa afisze linkuril prouduselor, in dreptul fiecarui link, sa afiseze un buton de procesare
 - in urma procesarii, sa iti afiseze inca un link, care sa te duca la noul produs
 - si sa mai afiseze 2 label-uri, cu profitabilitatea produsului, si cu nivelul de similitudine cu produsul original
 - camp in modelul de produs: Magazin, status (procesat, neprocesat), data la care a fost adaugat
 - de mutat proiectul inapoi, in propriul repository
 - link pentru procesare produse(  complete_fields)



Partea de scraping are 4 pasi:
1. Plecand de la denumirea unui produs, sau "", se cauta primele produse de pe Olx, si se salveaza link-urile
2. Se proceseaza link-urile, si se salveaza datele produselor (Completare campuri)
3. Se cauta produse similare, si se salveaza link-urile
4. Se proceseaza link-urile, si se salveaza datele produselor (Completare campuri)