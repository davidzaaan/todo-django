console.log('start render')

const message = document.querySelector('.alert');

const closeMessage = () => {
    message.remove()
}

const completeTaskBtn = document.getElementById('complete-task');
const deleteTaskBtn = document.getElementById('delete-task');

const completeTask = (id) => {

    fetch(`http://127.0.0.1:8000/api/task-complete/${id}/`, {
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

    fetch(`http://127.0.0.1:8000/api/task-delete/${id}/`, {
        method: 'DELETE',
    })
        .then(response => response.json())
        .then(data => console.log(data))

    console.log(`task with id ${id} was succesfully deleted`)
    window.location.reload()
}


console.log('end render')