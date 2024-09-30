import requests
from bs4 import BeautifulSoup

url = 'https://www.kinopoisk.ru/lists/movies/top250/'

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'lxml')
    movies = soup.find_all('div', class_='desktop-rating-selection-film-item')

    for movie in movies:
        title = movie.find('p', class_='selection-film-item-meta__name').text
        rating = movie.find('span', class_='rating__value').text
        print(f"Название: {title}, Рейтинг: {rating}")
else:
    print(f"Ошибка при запросе страницы. Код состояния: {response.status_code}")

    import requests
    from bs4 import BeautifulSoup
    import pandas as pd


    url = 'https://www.kinopoisk.ru/lists/movies/top250/'


    response = requests.get(url)


    if response.status_code == 200:
        html_content = response.text


        soup = BeautifulSoup(html_content, 'lxml')


        movies = soup.find_all('div', class_='desktop-rating-selection-film-item')


        if not movies:
            print("Не удалось найти фильмы на странице. Проверьте селекторы.")
        else:

            movie_titles = []
            movie_ratings = []


            for movie in movies:
                try:

                    title = movie.find('p', class_='selection-film-item-meta__name').text.strip()


                    rating = movie.find('span', class_='rating__value').text.strip()


                    movie_titles.append(title)
                    movie_ratings.append(rating)
                except AttributeError as e:
                    print(f"Ошибка при парсинге фильма: {e}")


            if movie_titles and movie_ratings:

                df = pd.DataFrame({
                    'Название фильма': movie_titles,
                    'Рейтинг': movie_ratings
                })


                df.to_excel('kinopoisk_top250.xlsx', index=False, engine='openpyxl')

                print("Данные успешно сохранены в файл kinopoisk_top250.xlsx")
            else:
                print("Не удалось собрать данные о фильмах.")
    else:
        print(f"Ошибка при запросе страницы. Код состояния: {response.status_code}")



