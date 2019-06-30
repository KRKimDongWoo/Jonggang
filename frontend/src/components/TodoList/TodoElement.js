import React, { Component } from 'react'
import moment from 'moment'

import './TodoList.css'

const styles = {
	curtain: 'jg-todo-element-curtain',
	curtainText: 'jg-todo-element-curtain__text',
	curtainButton: 'jg-todo-element-curtain__button',
	wrapper: 'jg-todo-element-wrapper',
	date: 'jg-todo-element-date',
	dateText: 'jg-todo-element-date__text',
	dateMonth: 'jg-todo-element-date__month',
	dateDay: 'jg-todo-element-date__day',
	dateTime: 'jg-todo-element-date__time',
	text: 'jg-todo-element-text',
	textTitle: 'jg-todo-element-text__title',
	textDescription: 'jg-todo-element-text__description',
	buttonset: 'jg-todo-element-buttonset',
	buttons: 'jg-todo-element-buttonset__button',
}

export default class TodoElement extends Component {
	render() {
		return (
			<div className={styles.wrapper}>
				{
					(this.props.done) ? (
						<div className={styles.curtain}> 
							<p className={styles.curtainText}> 완료되었습니다. </p>
							<button className={styles.curtainButton}> 취소 </button>
						</div>
					) : (null)
				}
				<div className={styles.date}>
					<p className={[styles.dateText, styles.dateMonth].join(' ')}>
						{moment(this.props.date).format('M월')}
					</p>
					<p className={[styles.dateText, styles.dateDay].join(' ')}>
						{moment(this.props.date).format('D')}
					</p>
					<p className={[styles.dateText, styles.dateTime].join(' ')}>
						{moment(this.props.date).format('h:mm A')}
					</p>									
				</div>
				<div className={styles.text}>
					<p className={styles.textTitle}>
						<strong> {this.props.course} </strong> {this.props.type}
					</p>
					<p className={styles.textDescription}>
						{this.props.memo}
					</p>
				</div>
				<div className={styles.buttonset}>
					<button className={styles.buttons}>
						수정
					</button>
					<button className={styles.buttons}>
						삭제
					</button>
					<button className={styles.buttons}>
						<strong> 완료 </strong>
					</button>
				</div>
			</div>
		)
	}
}
