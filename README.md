СТАРТ:
 1. git clone https://github.com/Miwacer/testTask.git
 2. cd testTask
 3. docker-compose build
 4. docker-compose up -d db
 5. docker-compose up get_data
 6. docker-compose up print_data
 
.env файл не використовується, всі змінні вже прописані в docker-compose.yml для спрощення запуску.
 
 result:
 <img width="1908" height="954" alt="image" src="https://github.com/user-attachments/assets/74b398de-b116-4d9b-95ad-13be6d54a620" />
