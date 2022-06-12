<template>
  <div class="container wrapper">
    <main class="px-3 content">
      <h2>Информация</h2>
      <p class="lead">
        {{ message }} <br>
        {{ info }}
      </p>
<!--      <p class="lead">-->
<!--        {{ info }}-->
<!--      </p>-->
      <div class="row justify-content-center">
        <div class="col-sm-4">
          <div class="card" style="width: auto;">
            <img src="../../public/search.png" class="card-img-top" alt="Поиск">
            <div class="card-body">
              <h5 class="card-title">Поиск по таблице</h5>
              <p class="card-text">Можно искать пользователей по имени, почте, группе и даже телефону. Для поиска надо просто заполнить специальное поле и найденные пользователи отобразятся.</p>
            </div>
          </div>
        </div>
        <div class="col-sm-4">
          <div class="card" style="width: auto;">
            <img src="../../public/sorting.png" class="card-img-top" alt="Сортировка">
            <div class="card-body">
              <h5 class="card-title">Сортировка</h5>
              <p class="card-text">Можно сортировать пользователей в таблице по любому интересующему вас полю. Для этого необходимо нажать на значок рядом с соответствующим столбцом.</p>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'WelcomePage',
  data() {
    return {
      message: 'Приветстувем вас, дорогой пользователь!',
      info: 'Этот веб-сервис содержит данные по пользователям и предоставляет следующие возможности.'
    }
  }
}
</script>

<style>
.px-3 {
  padding-right: 1rem!important;
  padding-left: 1rem!important;
  color: blueviolet;
}
.lead {
  font-size: 1.25rem;
  font-weight: 300;
}

p {
  margin-top: 0;
  margin-bottom: 1rem;
}
p {
  display: block;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}

.mt-auto {
  margin-top: auto!important;
}

/*.cards {*/
/*  margin-left: auto;*/
/*  margin-right: auto;*/
/*}*/

img {
  height: 210px;
  max-width: 250px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
}
</style>