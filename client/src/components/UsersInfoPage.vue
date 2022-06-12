<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-11">
        <h2>Фильтр поиска</h2>
        <div class="col-6" style="margin-left: auto; margin-right: auto">
          <input v-on:keyup="usersSearch" type="text" class="search form-control" id="search">
          <div id="searchHelp" class="form-text">Введите имя, почту, телефон или группу для поиска пользователя.</div>
        </div>
        <h2>Список пользователей</h2>
        <div id="sortHelp" class="form-text">Для сортировки данных нажмите на жёлтый значок сортировки рядом с соответствующим столбцом.</div>
        <table class="table table-hover table-bordered" id="usersInfoTable">
          <thead>
            <tr>
              <th></th>
              <th scope="col" >Полное имя
                <svg v-on:click="sortByFullName" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                </svg>
              </th>
              <th scope="col" v-on:click="sortByAccount">Учётная запись
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                </svg></th>
              <th scope="col" v-on:click="sortByEmail">Электронная почта
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                </svg></th>
              <th scope="col" v-on:click="sortByUserGroup">Группа
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                </svg></th>
              <th scope="col" v-on:click="sortByPhoneNumber">Телефон
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-down-up" viewBox="0 0 16 16">
                  <path fill-rule="evenodd" d="M11.5 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L11 2.707V14.5a.5.5 0 0 0 .5.5zm-7-14a.5.5 0 0 1 .5.5v11.793l3.146-3.147a.5.5 0 0 1 .708.708l-4 4a.5.5 0 0 1-.708 0l-4-4a.5.5 0 0 1 .708-.708L4 13.293V1.5a.5.5 0 0 1 .5-.5z"/>
                </svg></th>
            </tr>
          </thead>
          <tbody v-for="(user, index) in users" :key="index">
            <tr>
              <td>
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                  <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                  <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                </svg>
              </td>
              <td>{{ user.fullName }}</td>
              <td>{{ user.account }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.userGroup }}</td>
              <td>{{ user.phoneNumber }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UsersInfoPage',
  data() {
    return {
      users: []
    };
  },
  methods: {
    apiGetUsers() {
      axios
          .get('http://localhost:5000/users')
          .then(response => {
            this.users = response.data.users;
          })
          .catch(error => {
            console.log(error)
          })
    },
    usersSearch() {
      let searchText = document.getElementById('search');
      let table = document.getElementById('usersInfoTable');
      let regSearchText = new RegExp(searchText.value, 'i');
      let flag = false;
      for (let i = 1; i < table.rows.length; i++) {
        flag = false;
        for (let j = table.rows[i].cells.length - 1; j >= 0; j--) {
          flag = regSearchText.test(table.rows[i].cells[j].innerHTML);
          if (flag) break;
        }
        if (flag) {
          table.rows[i].style.display = "";
        } else {
          table.rows[i].style.display = "none";
        }
      }
    },
    sortByFullName() {
      this.users.sort((a, b) => a.fullName.localeCompare(b.fullName))
    },
    sortByAccount() {
      this.users.sort((a, b) => a.account.localeCompare(b.account))
    },
    sortByEmail() {
      this.users.sort((a, b) => a.email.localeCompare(b.email))
    },
    sortByUserGroup() {
      this.users.sort((a, b) => a.userGroup.localeCompare(b.userGroup))
    },
    sortByPhoneNumber() {
      this.users.sort((a, b) => a.phoneNumber.localeCompare(b.phoneNumber))
    }
  },
  created() {
    this.apiGetUsers();
  }
}
</script>

<style>
.container {
  margin-left: auto;
  margin-right: auto;
}

th {
  color: blueviolet;
}

th svg {
  color: goldenrod;
  cursor: pointer;
}

h2 {
  margin: 10px;
  color: blueviolet;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: bold;
}

#sortHelp {
  margin-bottom: 10px;
  font-size: 15px;
}
</style>