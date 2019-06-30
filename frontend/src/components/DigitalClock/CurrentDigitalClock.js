import React, { Component } from 'react'
import moment from 'moment'

import './DigitalClock.css'

export default class CurrentDigitalClock extends Component {

	state = {
		current: null,
	}

	constructor(props) {
		super(props)
		this.state.current = moment()

		setInterval(() => {
			this.setState({
				current: moment().toObject()
			})
		}, 1000)

	}

	createItem = (number, type) => {
		return (
			<div className='jg-digitalclock-items'>
				<div className='jg-digitalclock-items__numbers'>
					<p> {(isNaN(number)) ? 0 : parseInt(number / 10)} </p>
				</div>
				<div className='jg-digitalclock-items__numbers'>
					<p> {(isNaN(number)) ? 0 : number % 10} </p>
				</div>
				<div className='jg-digitalclock-items__types'>
					<p> {type} </p>
				</div>
			</div>
		)
	}

	render() {
		return (
			<div className='jg-digitalclock-wrapper'>
				{this.createItem(this.state.current.months, '월')}
				{this.createItem(this.state.current.date, '일')}
				<div className='jg-digitalclock-items__spacer' />
				{this.createItem(this.state.current.hours, '시')}
				{this.createItem(this.state.current.minutes, '분')}
				{this.createItem(this.state.current.seconds, '초')}
			</div>
		)
	}
}
