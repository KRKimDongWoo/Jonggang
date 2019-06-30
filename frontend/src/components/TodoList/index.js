import React, { Component } from 'react'

import TodoElement from './TodoElement'

import './TodoList.css'

class TodoList extends Component {
	state = {
		todos: [
			{
				id: 0,
				course: '시스템프로그래밍', 
				todo_type: '중간고사', 
				date: '2019-05-28T14:00',  
				memo: '',
				done: false,
			},
			{ 
				id: 1,
				course: '시스템프로그래밍', 
				todo_type: '과제',
				date: '2019-06-04T23:59',
				memo: '수정하기 근데 말을 많이 쓰다보면 이게 스크롤이 생겨야 될수도 있거든 그래서 어디 한번 해보자 그런 마음으로 일단 많이 메모를 작성해 봤음',
				done: true,
			}
		]
	}

	render() {
		return (
			<div className='jg-todo-list-wrapper'>
				<div className='jg-todo-list-header'>
					<h1 className='jg-todo-list-header__title'>
						일정
					</h1>
					<button className='jg-todo-list-header__button'>
						+
					</button>
				</div>
				<hr />
				<div className='jg-todo-list-body'>
					{
						this.state.todos.map( todo => (
							<TodoElement
								id={todo.id}
								course={todo.course}
								type={todo.todo_type}
								date={todo.date}
								memo={todo.memo}
								done={todo.done}
							/>
						))
					}
				</div>
			</div>
		)
	}
}

export default TodoList
