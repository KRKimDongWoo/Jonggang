import React, { Component } from 'react'
import moment from 'moment'

export default class DdayDigitalClock extends Component {
	
	state = {
		current: null,
		timeDiff: 0,
	}

	constructor(props) {
		super(props)
		this.state.current = moment()

		setInterval(() => {
			this.setState({
				timeDiff: -moment().diff(this.props.endDate, 'seconds'),
			})
		}, 1000)
	}

	createItem3 = (number, type) => {
		return (
			<div className='jg-digitalclock-items'>
				<div className='jg-digitalclock-items__numbers'>
					<p> {(isNaN(number)) ? 0 : parseInt(number / 100)} </p>
				</div>
				<div className='jg-digitalclock-items__numbers'>
					<p> {(isNaN(number)) ? 0 : parseInt(number / 10) % 10} </p>
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
				{this.createItem3(parseInt(this.state.timeDiff / 60 / 60 / 24), '일')}
				{this.createItem(parseInt(this.state.timeDiff / 60 / 60) % 24, '시간')}
				{this.createItem(parseInt(this.state.timeDiff / 60 % 60), '분')}
				{this.createItem(parseInt(this.state.timeDiff) % 60, '초')}
			</div>
		)
	}
}

