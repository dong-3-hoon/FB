import Vue from "vue";
import Vuex from "vuex";
import _ from 'lodash';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		orderList: [],
		optionList: [
			{
				type: "샷  ",
				price: 500,
				count: 0,
			},
			{
				type: "바닐라 시럽",
				price: 1000,
				count: 0,
			},
			{
				type: "카라멜 시럽",
				price: 1500,
				count: 0,
			}
		],
		menuList: [
			{
				title: "아메리카노",
				price: 3000,
				selected: false,
				image: "https://source.unsplash.com/featured/?americano",
			},
			{
				title: "라떼",
				price: 4000,
				selected: false,
				image: "https://source.unsplash.com/featured/?latte",
			},
			{
				title: "카푸치노",
				price: 4500,
				selected: false,
				image: "https://source.unsplash.com/featured/?capucchino",
			},
		],
		sizeList: [
			{
				name: "small",
				price: 0,
				selected: false,
			},
			{
				name: "medium",
				price: 500,
				selected: false,
			},
			{
				name: "large",
				price: 1000,
				selected: false,
			},
		],
		selectedOption: {},
		selectedMenu: {},
		selectedSize: {},
	},
	getters: {
		totalOrderCount(state) {
			return state.orderList.length;
		},
		totalOrderPrice(state) {
			return state.orderList.reduce((sum, order) => {
				sum += order.menu.price + order.size.price;
				for(const option of order.option){
					sum += option.count*option.price
				}
				return sum;
			}, 0);
		},
	},
	mutations: {
		addOrder(state) {
			state.orderList.push({
				menu: state.selectedMenu,
				size: state.selectedSize,
				option: _.cloneDeep(state.optionList),
			})
		},
		updateMenuList(state, selectedMenu) {
			state.menuList = state.menuList.map((menu) => {
				if (menu.title === selectedMenu.title) {
					menu.selected = true;
					state.selectedMenu = selectedMenu;
				} else {
					menu.selected = false;
				}
				return menu;
			});
		},
		updateSizeList(state, selectedSize) {
			state.sizeList = state.sizeList.map((size) => {
				if (size.name === selectedSize.name) {
					size.selected = true;
					state.selectedSize = selectedSize;
				} else {
					size.selected = false;
				}
				return size;
			});
		},
		updateOtionList(state, selectedOption){
			state.optionList = state.optionList.map((option)=>{
				if(option.type===selectedOption.type){
					option.selected = true;
					state.selectedOption = selectedOption;
				}
				else{
					option.selected = false;
				}
				return option;
			})
		}
	},
	actions: {
		selectMenu(context, selectedMenu) {
			context.commit("updateMenuList", selectedMenu);
		},
		selectSize(context, selectedSize) {
			context.commit("updateSizeList", selectedSize);
		},
		selectOption(context, selectedOption) {
			context.commit("updateOptionList", selectedOption);
		},
		addOrder(context) {
			context.commit("addOrder");
		},
	},
	modules: {},
});
