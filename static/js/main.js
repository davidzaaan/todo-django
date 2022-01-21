console.log('start render')

const message = document.querySelector('.alert');

const closeMessage = () => {
    message.remove()
}

const completeTaskBtn = document.getElementById('complete-task');
const deleteTaskBtn = document.getElementById('delete-task');

const completeTask = (id) => {

    fetch(`https://todo-django-dm.herokuapp.com/api/task-complete/${id}/`, {
        method: 'PATCH',
        // headers: {
        //     'Content-Type': 'application/json',
        //     // Authorization: `token ${document.cookie}`
        // }
    })
        .then(response => response.json())
        .then(data => console.log(data))

    console.log(`task with id ${id} was succesfully completed`)
    window.location.reload()
}

const deleteTask = (id) => {

    fetch(`https://todo-django-dm.herokuapp.com/api/task-delete/${id}/`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => console.log(data))

    console.log(`task with id ${id} was succesfully deleted`)
    window.location.reload()
}


console.log('end render')