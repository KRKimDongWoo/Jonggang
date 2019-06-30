import React, { Component } from 'react'
import moment from 'moment'

import {
	CurrentDigitalClock,
	DdayDigitalClock,
} from 'components/DigitalClock'
import TodoList from 'components/TodoList'

import './MainContainer.css'

class MainContainer extends Component {

	state = {
		endDate: moment('2019-08-03T00:00')
	}

	render() {
		return (
			<div className='jg-main-container-wrapper'>
				<div className='jg-main-container'>
					<div className='jg-main-container-header'>
						<h1 className='jg-main-container-header__title'> JONGGANG </h1>
					</div>
					<div className='jg-main-container__timer'>
						<h1 className='jg-main-container__timer-title'> 현재 시각 </h1>
						<div className='jg-main-container__timer-clock'>
							<CurrentDigitalClock />
						</div>
					</div>
					<div className='jg-main-container__timer'>					
						<h1 className='jg-main-container__timer-title'> 종강까지 </h1>
						<div className='jg-main-container__timer-clock'>
							<DdayDigitalClock endDate={this.state.endDate} />
						</div>
					</div>
					<div className='jg-main-container__todos'>
						<TodoList />
					</div>
				</div>
			</div>
		)
	}
}

export default MainContainer
