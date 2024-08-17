def findDecision(obj): #obj[0]: Sand %, obj[1]: Clay %, obj[2]: Silt %, obj[3]: pH, obj[4]: EC mS/cm, obj[5]: O.M. %, obj[6]: CACO3 %, obj[7]: N_NO3 ppm, obj[8]: P ppm, obj[9]: K ppm , obj[10]: Mg ppm, obj[11]: Fe ppm, obj[12]: Zn ppm, obj[13]: Mn ppm, obj[14]: Cu ppm, obj[15]: B ppm, obj[16]: Crop, obj[17]: Salinity
	# {"feature": "Crop", "instances": 780, "metric_value": 3.3125, "depth": 1}
	if obj[16] == 'paddy':
		# {"feature": "Cu ppm", "instances": 43, "metric_value": 2.351, "depth": 2}
		if obj[14] == '<=2.79':
			# {"feature": "Silt %", "instances": 41, "metric_value": 2.2333, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "EC mS/cm", "instances": 40, "metric_value": 2.2368, "depth": 4}
				if obj[4] == '>0.321':
					# {"feature": "O.M. %", "instances": 39, "metric_value": 2.2373, "depth": 5}
					if obj[5] == '>0.99':
						# {"feature": "N_NO3 ppm", "instances": 38, "metric_value": 2.234, "depth": 6}
						if obj[7] == '<=26.86':
							# {"feature": "P ppm", "instances": 36, "metric_value": 2.2039, "depth": 7}
							if obj[8] == '<=38.29':
								# {"feature": "K ppm ", "instances": 33, "metric_value": 2.2066, "depth": 8}
								if obj[9] == '<=551':
									# {"feature": "pH", "instances": 31, "metric_value": 2.2494, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "CACO3 %", "instances": 30, "metric_value": 2.2683, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "Clay %", "instances": 29, "metric_value": 2.2528, "depth": 11}
											if obj[1] == '<=44.8':
												# {"feature": "B ppm", "instances": 24, "metric_value": 2.1473, "depth": 12}
												if obj[15] == '>0.16':
													# {"feature": "Zn ppm", "instances": 23, "metric_value": 2.1769, "depth": 13}
													if obj[12] == '<=0.55':
														# {"feature": "Mn ppm", "instances": 17, "metric_value": 2.2569, "depth": 14}
														if obj[13] == '<=12.1':
															# {"feature": "Fe ppm", "instances": 15, "metric_value": 2.1819, "depth": 15}
															if obj[11] == '<=22.65':
																# {"feature": "Salinity", "instances": 13, "metric_value": 2.1339, "depth": 16}
																if obj[17] == '>3.9':
																	# {"feature": "Mg ppm", "instances": 9, "metric_value": 1.8366, "depth": 17}
																	if obj[10] == '<=701':
																		# {"feature": "Sand %", "instances": 5, "metric_value": 1.371, "depth": 18}
																		if obj[0] == '>12.0':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	elif obj[10] == '>701':
																		# {"feature": "Sand %", "instances": 4, "metric_value": 2.0, "depth": 18}
																		if obj[0] == '>12.0':
																			return 'Poultry Manure'
																		else: return 'Poultry Manure'
																	else: return 'Poultry Manure'
																elif obj[17] == '<=3.9':
																	# {"feature": "Sand %", "instances": 4, "metric_value": 2.0, "depth": 17}
																	if obj[0] == '>12.0':
																		# {"feature": "Mg ppm", "instances": 4, "metric_value": 2.0, "depth": 18}
																		if obj[10] == '<=701':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															elif obj[11] == '>22.65':
																# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10] == '<=701':
																	return 'Poultry Manure'
																elif obj[10] == '>701':
																	return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Poultry Manure'
														elif obj[13] == '>12.1':
															# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10] == '>701':
																return 'Compost'
															elif obj[10] == '<=701':
																return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Compost'
													elif obj[12] == '>0.55':
														# {"feature": "Fe ppm", "instances": 6, "metric_value": 1.4591, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mg ppm", "instances": 4, "metric_value": 0.8113, "depth": 15}
															if obj[10] == '<=701':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[0] == '>12.0':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																elif obj[13] == '<=12.1':
																	return 'Cow Manure'
																else: return 'Cow Manure'
															elif obj[10] == '>701':
																return 'Cow Manure'
															else: return 'Cow Manure'
														elif obj[11] == '<=22.65':
															# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[0] == '>12.0':
																# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10] == '>701':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'Cow Manure'
												elif obj[15] == '<=0.16':
													return 'Cow Manure'
												else: return 'Cow Manure'
											elif obj[1] == '>44.8':
												# {"feature": "Zn ppm", "instances": 5, "metric_value": 1.9219, "depth": 12}
												if obj[12] == '<=0.55':
													# {"feature": "Mg ppm", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[10] == '>701':
														return 'Compost'
													elif obj[10] == '<=701':
														return 'Green Manure'
													else: return 'Green Manure'
												elif obj[12] == '>0.55':
													# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[17] == '>3.9':
														return 'Poultry Manure'
													elif obj[17] == '<=3.9':
														return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'Poultry Manure'
											else: return 'Compost'
										elif obj[6] == '>28.3':
											return 'Poultry Manure'
										else: return 'Poultry Manure'
									elif obj[3] == '>7.79':
										return 'Cow Manure'
									else: return 'Cow Manure'
								elif obj[9] == '>551':
									return 'Cow Manure'
								else: return 'Cow Manure'
							elif obj[8] == '>38.29':
								# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[13] == '<=12.1':
									return 'Poultry Manure'
								elif obj[13] == '>12.1':
									return 'Cow Manure'
								else: return 'Cow Manure'
							else: return 'Poultry Manure'
						elif obj[7] == '>26.86':
							# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[10] == '>701':
								return 'Compost'
							elif obj[10] == '<=701':
								return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'Compost'
					elif obj[5] == '<=0.99':
						return 'VermiCompost'
					else: return 'VermiCompost'
				elif obj[4] == '<=0.321':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[2] == '>50.0':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[14] == '>2.79':
			# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[6] == '>28.3':
				return 'Farmyard Manure'
			elif obj[6] == '<=28.3':
				return 'Green Manure'
			else: return 'Green Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == ' groundnut':
		# {"feature": "Silt %", "instances": 41, "metric_value": 2.5559, "depth": 2}
		if obj[2] == '<=50.0':
			# {"feature": "Sand %", "instances": 40, "metric_value": 2.5477, "depth": 3}
			if obj[0] == '>12.0':
				# {"feature": "Clay %", "instances": 38, "metric_value": 2.5703, "depth": 4}
				if obj[1] == '<=44.8':
					# {"feature": "Mn ppm", "instances": 32, "metric_value": 2.5187, "depth": 5}
					if obj[13] == '<=12.1':
						# {"feature": "Fe ppm", "instances": 26, "metric_value": 2.4745, "depth": 6}
						if obj[11] == '<=22.65':
							# {"feature": "Mg ppm", "instances": 24, "metric_value": 2.4073, "depth": 7}
							if obj[10] == '<=701':
								# {"feature": "K ppm ", "instances": 21, "metric_value": 2.2418, "depth": 8}
								if obj[9] == '<=551':
									# {"feature": "Cu ppm", "instances": 19, "metric_value": 2.1816, "depth": 9}
									if obj[14] == '<=2.79':
										# {"feature": "pH", "instances": 15, "metric_value": 2.0662, "depth": 10}
										if obj[3] == '>7.79':
											# {"feature": "Zn ppm", "instances": 9, "metric_value": 1.4355, "depth": 11}
											if obj[12] == '<=0.55':
												# {"feature": "B ppm", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[15] == '>0.16':
													return 'Farmyard Manure'
												elif obj[15] == '<=0.16':
													# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6] == '>28.3':
														return 'Cow Manure'
													elif obj[6] == '<=28.3':
														return 'Farmyard Manure'
													else: return 'Farmyard Manure'
												else: return 'Cow Manure'
											elif obj[12] == '>0.55':
												# {"feature": "CACO3 %", "instances": 4, "metric_value": 1.5, "depth": 12}
												if obj[6] == '>28.3':
													# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == '<=26.86':
														return 'Farmyard Manure'
													elif obj[7] == '>26.86':
														return 'VermiCompost'
													else: return 'VermiCompost'
												elif obj[6] == '<=28.3':
													# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[15] == '<=0.16':
														return 'VermiCompost'
													elif obj[15] == '>0.16':
														return 'Cow Manure'
													else: return 'Cow Manure'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										elif obj[3] == '<=7.79':
											# {"feature": "Zn ppm", "instances": 6, "metric_value": 1.9183, "depth": 11}
											if obj[12] == '<=0.55':
												# {"feature": "CACO3 %", "instances": 5, "metric_value": 1.5219, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "EC mS/cm", "instances": 4, "metric_value": 1.5, "depth": 13}
													if obj[4] == '>0.321':
														# {"feature": "O.M. %", "instances": 4, "metric_value": 1.5, "depth": 14}
														if obj[5] == '>0.99':
															# {"feature": "N_NO3 ppm", "instances": 4, "metric_value": 1.5, "depth": 15}
															if obj[7] == '<=26.86':
																# {"feature": "P ppm", "instances": 4, "metric_value": 1.5, "depth": 16}
																if obj[8] == '<=38.29':
																	# {"feature": "B ppm", "instances": 4, "metric_value": 1.5, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 4, "metric_value": 1.5, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												elif obj[6] == '>28.3':
													return 'VermiCompost'
												else: return 'VermiCompost'
											elif obj[12] == '>0.55':
												return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Cow Manure'
									elif obj[14] == '>2.79':
										# {"feature": "Zn ppm", "instances": 4, "metric_value": 1.5, "depth": 10}
										if obj[12] == '>0.55':
											# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == '>7.79':
												# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[15] == '<=0.16':
													return 'Farmyard Manure'
												elif obj[15] == '>0.16':
													return 'Neem Cake'
												else: return 'Neem Cake'
											elif obj[3] == '<=7.79':
												return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										elif obj[12] == '<=0.55':
											return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'Farmyard Manure'
								elif obj[9] == '>551':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										return 'Poultry Manure'
									elif obj[3] == '>7.79':
										return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'Poultry Manure'
							elif obj[10] == '>701':
								# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6] == '>28.3':
										return 'Compost'
									elif obj[6] == '<=28.3':
										return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								elif obj[3] == '>7.79':
									return 'Poultry Manure'
								else: return 'Poultry Manure'
							else: return 'Compost'
						elif obj[11] == '>22.65':
							# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == '>7.79':
								return 'Compost'
							elif obj[3] == '<=7.79':
								return 'Cow Manure'
							else: return 'Cow Manure'
						else: return 'Compost'
					elif obj[13] == '>12.1':
						# {"feature": "Mg ppm", "instances": 6, "metric_value": 1.7925, "depth": 6}
						if obj[10] == '>701':
							# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4] == '>0.321':
								# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[12] == '>0.55':
									return 'Compost'
								elif obj[12] == '<=0.55':
									return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[4] == '<=0.321':
								return 'Compost'
							else: return 'Compost'
						elif obj[10] == '<=701':
							# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4] == '<=0.321':
									return 'Farmyard Manure'
								elif obj[4] == '>0.321':
									return 'Poultry Manure'
								else: return 'Poultry Manure'
							elif obj[3] == '>7.79':
								return 'Compost'
							else: return 'Compost'
						else: return 'Compost'
					else: return 'Compost'
				elif obj[1] == '>44.8':
					# {"feature": "Fe ppm", "instances": 6, "metric_value": 1.7925, "depth": 5}
					if obj[11] == '<=22.65':
						# {"feature": "Mn ppm", "instances": 5, "metric_value": 1.371, "depth": 6}
						if obj[13] == '<=12.1':
							# {"feature": "pH", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[3] == '>7.79':
								return 'Compost'
							elif obj[3] == '<=7.79':
								# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[15] == '<=0.16':
									return 'Compost'
								elif obj[15] == '>0.16':
									return 'Green Manure'
								else: return 'Green Manure'
							else: return 'Compost'
						elif obj[13] == '>12.1':
							return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[11] == '>22.65':
						return 'Poultry Manure'
					else: return 'Poultry Manure'
				else: return 'Compost'
			elif obj[0] == '<=12.0':
				return 'Compost'
			else: return 'Compost'
		elif obj[2] == '>50.0':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == ' paddy':
		# {"feature": "B ppm", "instances": 39, "metric_value": 2.7041, "depth": 2}
		if obj[15] == '>0.16':
			# {"feature": "EC mS/cm", "instances": 36, "metric_value": 2.7177, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "CACO3 %", "instances": 31, "metric_value": 2.6758, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "N_NO3 ppm", "instances": 23, "metric_value": 2.5121, "depth": 5}
					if obj[7] == '<=26.86':
						# {"feature": "P ppm", "instances": 21, "metric_value": 2.4983, "depth": 6}
						if obj[8] == '<=38.29':
							# {"feature": "Cu ppm", "instances": 20, "metric_value": 2.4955, "depth": 7}
							if obj[14] == '<=2.79':
								# {"feature": "Clay %", "instances": 16, "metric_value": 2.3829, "depth": 8}
								if obj[1] == '<=44.8':
									# {"feature": "Fe ppm", "instances": 11, "metric_value": 2.2222, "depth": 9}
									if obj[11] == '>22.65':
										# {"feature": "Mg ppm", "instances": 6, "metric_value": 1.2516, "depth": 10}
										if obj[10] == '<=701':
											# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[17] == '<=3.9':
													return 'VermiCompost'
												elif obj[17] == '>3.9':
													return 'Poultry Manure'
												else: return 'Poultry Manure'
											elif obj[3] == '>7.79':
												return 'Poultry Manure'
											else: return 'Poultry Manure'
										elif obj[10] == '>701':
											# {"feature": "Zn ppm", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[12] == '>0.55':
												# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[17] == '>3.9':
													return 'Compost'
												elif obj[17] == '<=3.9':
													return 'Poultry Manure'
												else: return 'Poultry Manure'
											elif obj[12] == '<=0.55':
												return 'Poultry Manure'
											else: return 'Poultry Manure'
										else: return 'Poultry Manure'
									elif obj[11] == '<=22.65':
										# {"feature": "pH", "instances": 5, "metric_value": 1.9219, "depth": 10}
										if obj[3] == '<=7.79':
											# {"feature": "Zn ppm", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[12] == '<=0.55':
												# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5] == '>0.99':
															# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10] == '<=701':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Poultry Manure'
																		else: return 'Poultry Manure'
																	else: return 'Poultry Manure'
																else: return 'Poultry Manure'
															else: return 'Poultry Manure'
														else: return 'Poultry Manure'
													else: return 'Poultry Manure'
												else: return 'Poultry Manure'
											elif obj[12] == '>0.55':
												return 'Cow Manure'
											else: return 'Cow Manure'
										elif obj[3] == '>7.79':
											# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[12] == '<=0.55':
												return 'Farmyard Manure'
											elif obj[12] == '>0.55':
												return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Farmyard Manure'
									else: return 'Green Manure'
								elif obj[1] == '>44.8':
									# {"feature": "pH", "instances": 5, "metric_value": 1.5219, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "K ppm ", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[9] == '<=551':
											# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[11] == '<=22.65':
												# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[17] == '>3.9':
													return 'Farmyard Manure'
												elif obj[17] == '<=3.9':
													return 'VermiCompost'
												else: return 'VermiCompost'
											elif obj[11] == '>22.65':
												return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										elif obj[9] == '>551':
											return 'VermiCompost'
										else: return 'VermiCompost'
									elif obj[3] == '>7.79':
										return 'Green Manure'
									else: return 'Green Manure'
								else: return 'Farmyard Manure'
							elif obj[14] == '>2.79':
								# {"feature": "pH", "instances": 4, "metric_value": 1.5, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "Zn ppm", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[12] == '>0.55':
										return 'Cow Manure'
									elif obj[12] == '<=0.55':
										return 'Compost'
									else: return 'Compost'
								elif obj[3] == '>7.79':
									return 'Poultry Manure'
								else: return 'Poultry Manure'
							else: return 'Cow Manure'
						elif obj[8] == '>38.29':
							return 'Green Manure'
						else: return 'Green Manure'
					elif obj[7] == '>26.86':
						# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8] == '<=38.29':
							return 'Farmyard Manure'
						elif obj[8] == '>38.29':
							return 'Cow Manure'
						else: return 'Cow Manure'
					else: return 'Farmyard Manure'
				elif obj[6] == '>28.3':
					# {"feature": "Cu ppm", "instances": 8, "metric_value": 1.75, "depth": 5}
					if obj[14] == '<=2.79':
						# {"feature": "N_NO3 ppm", "instances": 7, "metric_value": 1.3788, "depth": 6}
						if obj[7] == '<=26.86':
							# {"feature": "pH", "instances": 6, "metric_value": 1.2516, "depth": 7}
							if obj[3] == '>7.79':
								# {"feature": "Zn ppm", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12] == '>0.55':
									# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[17] == '>3.9':
										return 'Fish Emulsion'
									elif obj[17] == '<=3.9':
										return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								elif obj[12] == '<=0.55':
									return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							elif obj[3] == '<=7.79':
								# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[11] == '>22.65':
									return 'Farmyard Manure'
								elif obj[11] == '<=22.65':
									return 'Compost'
								else: return 'Compost'
							else: return 'Farmyard Manure'
						elif obj[7] == '>26.86':
							return 'Fish Emulsion'
						else: return 'Fish Emulsion'
					elif obj[14] == '>2.79':
						return 'Cow Manure'
					else: return 'Cow Manure'
				else: return 'Farmyard Manure'
			elif obj[4] == '<=0.321':
				# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.5219, "depth": 4}
				if obj[10] == '>701':
					# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == '<=44.8':
						return 'Cow Manure'
					elif obj[1] == '>44.8':
						return 'Fish Emulsion'
					else: return 'Fish Emulsion'
				elif obj[10] == '<=701':
					return 'VermiCompost'
				else: return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[15] == '<=0.16':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == 'cotton':
		# {"feature": "O.M. %", "instances": 31, "metric_value": 2.3894, "depth": 2}
		if obj[5] == '>0.99':
			# {"feature": "B ppm", "instances": 30, "metric_value": 2.2566, "depth": 3}
			if obj[15] == '>0.16':
				# {"feature": "P ppm", "instances": 28, "metric_value": 2.182, "depth": 4}
				if obj[8] == '<=38.29':
					# {"feature": "CACO3 %", "instances": 26, "metric_value": 2.162, "depth": 5}
					if obj[6] == '<=28.3':
						# {"feature": "Clay %", "instances": 24, "metric_value": 2.1887, "depth": 6}
						if obj[1] == '<=44.8':
							# {"feature": "N_NO3 ppm", "instances": 19, "metric_value": 2.0632, "depth": 7}
							if obj[7] == '<=26.86':
								# {"feature": "EC mS/cm", "instances": 18, "metric_value": 2.0441, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "Mg ppm", "instances": 15, "metric_value": 1.9069, "depth": 9}
									if obj[10] == '>701':
										# {"feature": "Zn ppm", "instances": 10, "metric_value": 1.9219, "depth": 10}
										if obj[12] == '<=0.55':
											# {"feature": "Mn ppm", "instances": 7, "metric_value": 1.9502, "depth": 11}
											if obj[13] == '<=12.1':
												# {"feature": "Sand %", "instances": 4, "metric_value": 1.5, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 4, "metric_value": 1.5, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "pH", "instances": 4, "metric_value": 1.5, "depth": 14}
														if obj[3] == '<=7.79':
															# {"feature": "K ppm ", "instances": 4, "metric_value": 1.5, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Fe ppm", "instances": 4, "metric_value": 1.5, "depth": 16}
																if obj[11] == '<=22.65':
																	# {"feature": "Cu ppm", "instances": 4, "metric_value": 1.5, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 4, "metric_value": 1.5, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											elif obj[13] == '>12.1':
												# {"feature": "Fe ppm", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[11] == '>22.65':
													# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0] == '>12.0':
														# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2] == '<=50.0':
															# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[3] == '<=7.79':
																# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9] == '<=551':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												elif obj[11] == '<=22.65':
													return 'Cow Manure'
												else: return 'Cow Manure'
											else: return 'Cow Manure'
										elif obj[12] == '>0.55':
											# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[13] == '>12.1':
												# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[3] == '<=7.79':
															# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[11] == '>22.65':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												else: return 'Cow Manure'
											elif obj[13] == '<=12.1':
												return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Green Manure'
									elif obj[10] == '<=701':
										# {"feature": "Zn ppm", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[12] == '<=0.55':
											return 'Green Manure'
										elif obj[12] == '>0.55':
											# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0] == '>12.0':
												# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[2] == '<=50.0':
													# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3] == '<=7.79':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Green Manure'
								elif obj[4] == '<=0.321':
									# {"feature": "Mg ppm", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[10] == '<=701':
										# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[12] == '<=0.55':
											return 'Cow Manure'
										elif obj[12] == '>0.55':
											return 'Poultry Manure'
										else: return 'Poultry Manure'
									elif obj[10] == '>701':
										return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[7] == '>26.86':
								return 'Poultry Manure'
							else: return 'Poultry Manure'
						elif obj[1] == '>44.8':
							# {"feature": "Zn ppm", "instances": 5, "metric_value": 1.371, "depth": 7}
							if obj[12] == '>0.55':
								# {"feature": "EC mS/cm", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7] == '<=26.86':
										# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[13] == '>12.1':
											return 'VermiCompost'
										elif obj[13] == '<=12.1':
											return 'Cow Manure'
										else: return 'Cow Manure'
									elif obj[7] == '>26.86':
										return 'Cow Manure'
									else: return 'Cow Manure'
								elif obj[4] == '<=0.321':
									return 'Cow Manure'
								else: return 'Cow Manure'
							elif obj[12] == '<=0.55':
								return 'Compost'
							else: return 'Compost'
						else: return 'Cow Manure'
					elif obj[6] == '>28.3':
						return 'Cow Manure'
					else: return 'Cow Manure'
				elif obj[8] == '>38.29':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			elif obj[15] == '<=0.16':
				return 'Compost'
			else: return 'Compost'
		elif obj[5] == '<=0.99':
			return 'Composted pine needles'
		else: return 'Composted pine needles'
	elif obj[16] == 'groundnut':
		# {"feature": "pH", "instances": 30, "metric_value": 2.5139, "depth": 2}
		if obj[3] == '<=7.79':
			# {"feature": "Cu ppm", "instances": 27, "metric_value": 2.4165, "depth": 3}
			if obj[14] == '<=2.79':
				# {"feature": "B ppm", "instances": 25, "metric_value": 2.3926, "depth": 4}
				if obj[15] == '>0.16':
					# {"feature": "P ppm", "instances": 22, "metric_value": 2.2128, "depth": 5}
					if obj[8] == '<=38.29':
						# {"feature": "Salinity", "instances": 20, "metric_value": 2.2527, "depth": 6}
						if obj[17] == '>3.9':
							# {"feature": "K ppm ", "instances": 19, "metric_value": 2.2598, "depth": 7}
							if obj[9] == '<=551':
								# {"feature": "Clay %", "instances": 17, "metric_value": 2.2184, "depth": 8}
								if obj[1] == '<=44.8':
									# {"feature": "Zn ppm", "instances": 10, "metric_value": 1.8464, "depth": 9}
									if obj[12] == '<=0.55':
										# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[10] == '<=701':
											# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[4] == '>0.321':
												return 'Compost'
											elif obj[4] == '<=0.321':
												return 'Cow Manure'
											else: return 'Cow Manure'
										elif obj[10] == '>701':
											# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[11] == '>22.65':
												return 'Cow Manure'
											elif obj[11] == '<=22.65':
												return 'Poultry Manure'
											else: return 'Poultry Manure'
										else: return 'Cow Manure'
									elif obj[12] == '>0.55':
										# {"feature": "EC mS/cm", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[4] == '>0.321':
											# {"feature": "Mg ppm", "instances": 4, "metric_value": 1.5, "depth": 11}
											if obj[10] == '>701':
												# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5] == '>0.99':
															# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[6] == '<=28.3':
																# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7] == '<=26.86':
																	# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11] == '>22.65':
																		# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13] == '>12.1':
																			return 'Poultry Manure'
																		else: return 'Poultry Manure'
																	else: return 'Poultry Manure'
																else: return 'Poultry Manure'
															else: return 'Poultry Manure'
														else: return 'Poultry Manure'
													else: return 'Poultry Manure'
												else: return 'Poultry Manure'
											elif obj[10] == '<=701':
												# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5] == '>0.99':
															# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[6] == '<=28.3':
																# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[7] == '<=26.86':
																	# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[11] == '>22.65':
																		# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[13] == '>12.1':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											else: return 'Green Manure'
										elif obj[4] == '<=0.321':
											return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								elif obj[1] == '>44.8':
									# {"feature": "Mg ppm", "instances": 7, "metric_value": 1.9502, "depth": 9}
									if obj[10] == '>701':
										# {"feature": "Fe ppm", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[11] == '<=22.65':
											# {"feature": "Zn ppm", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[12] == '<=0.55':
												# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[13] == '<=12.1':
													# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0] == '>12.0':
														# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[2] == '<=50.0':
															# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[4] == '>0.321':
																# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[5] == '>0.99':
																	# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[6] == '<=28.3':
																		# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[7] == '<=26.86':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												elif obj[13] == '>12.1':
													return 'Green Manure'
												else: return 'Green Manure'
											elif obj[12] == '>0.55':
												return 'Compost'
											else: return 'Compost'
										elif obj[11] == '>22.65':
											return 'Cow Manure'
										else: return 'Cow Manure'
									elif obj[10] == '<=701':
										return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[9] == '>551':
								# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1] == '>44.8':
									return 'Poultry Manure'
								elif obj[1] == '<=44.8':
									return 'VermiCompost'
								else: return 'VermiCompost'
							else: return 'Poultry Manure'
						elif obj[17] == '<=3.9':
							return 'Poultry Manure'
						else: return 'Poultry Manure'
					elif obj[8] == '>38.29':
						return 'Poultry Manure'
					else: return 'Poultry Manure'
				elif obj[15] == '<=0.16':
					# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == '>44.8':
						return 'Cow Manure'
					elif obj[1] == '<=44.8':
						return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				else: return 'Cow Manure'
			elif obj[14] == '>2.79':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[3] == '>7.79':
			# {"feature": "CACO3 %", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6] == '<=28.3':
				# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[11] == '>22.65':
					return 'Farmyard Manure'
				elif obj[11] == '<=22.65':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[6] == '>28.3':
				return 'Farmyard Manure'
			else: return 'Farmyard Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == ' maize':
		# {"feature": "N_NO3 ppm", "instances": 30, "metric_value": 2.8683, "depth": 2}
		if obj[7] == '<=26.86':
			# {"feature": "Mn ppm", "instances": 28, "metric_value": 2.7215, "depth": 3}
			if obj[13] == '<=12.1':
				# {"feature": "EC mS/cm", "instances": 16, "metric_value": 2.43, "depth": 4}
				if obj[4] == '>0.321':
					# {"feature": "Sand %", "instances": 13, "metric_value": 2.2955, "depth": 5}
					if obj[0] == '>12.0':
						# {"feature": "pH", "instances": 12, "metric_value": 2.2925, "depth": 6}
						if obj[3] == '<=7.79':
							# {"feature": "B ppm", "instances": 10, "metric_value": 2.2464, "depth": 7}
							if obj[15] == '>0.16':
								# {"feature": "Fe ppm", "instances": 7, "metric_value": 1.8424, "depth": 8}
								if obj[11] == '<=22.65':
									# {"feature": "Mg ppm", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[10] == '<=701':
										# {"feature": "Cu ppm", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[14] == '<=2.79':
											return 'Chicken Manure'
										elif obj[14] == '>2.79':
											return 'Cow Manure'
										else: return 'Cow Manure'
									elif obj[10] == '>701':
										return 'Cow Manure'
									else: return 'Cow Manure'
								elif obj[11] == '>22.65':
									# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[1] == '>44.8':
										# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == '>28.3':
											return 'Farmyard Manure'
										elif obj[6] == '<=28.3':
											return 'Cow Manure'
										else: return 'Cow Manure'
									elif obj[1] == '<=44.8':
										return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							elif obj[15] == '<=0.16':
								# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[1] == '<=44.8':
									# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[12] == '<=0.55':
										return 'Compost'
									elif obj[12] == '>0.55':
										return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								elif obj[1] == '>44.8':
									return 'Green Manure'
								else: return 'Green Manure'
							else: return 'Compost'
						elif obj[3] == '>7.79':
							# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[11] == '<=22.65':
								return 'Compost'
							elif obj[11] == '>22.65':
								return 'Green Manure'
							else: return 'Green Manure'
						else: return 'Compost'
					elif obj[0] == '<=12.0':
						return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				elif obj[4] == '<=0.321':
					# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == '<=7.79':
						# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[10] == '>701':
							return 'Compost'
						elif obj[10] == '<=701':
							return 'Bone Meal'
						else: return 'Bone Meal'
					elif obj[3] == '>7.79':
						return 'Compost'
					else: return 'Compost'
				else: return 'Compost'
			elif obj[13] == '>12.1':
				# {"feature": "Clay %", "instances": 12, "metric_value": 1.9591, "depth": 4}
				if obj[1] == '<=44.8':
					# {"feature": "pH", "instances": 10, "metric_value": 1.571, "depth": 5}
					if obj[3] == '<=7.79':
						# {"feature": "Mg ppm", "instances": 9, "metric_value": 1.2244, "depth": 6}
						if obj[10] == '<=701':
							# {"feature": "Fe ppm", "instances": 5, "metric_value": 1.5219, "depth": 7}
							if obj[11] == '>22.65':
								# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[15] == '<=0.16':
										return 'Farmyard Manure'
									elif obj[15] == '>0.16':
										return 'VermiCompost'
									else: return 'VermiCompost'
								elif obj[4] == '<=0.321':
									return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							elif obj[11] == '<=22.65':
								# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == '<=50.0':
										# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == '>0.321':
											# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12] == '<=0.55':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Poultry Manure'
																		else: return 'Poultry Manure'
																	else: return 'Poultry Manure'
																else: return 'Poultry Manure'
															else: return 'Poultry Manure'
														else: return 'Poultry Manure'
													else: return 'Poultry Manure'
												else: return 'Poultry Manure'
											else: return 'Poultry Manure'
										else: return 'Poultry Manure'
									else: return 'Poultry Manure'
								else: return 'Poultry Manure'
							else: return 'Poultry Manure'
						elif obj[10] == '>701':
							return 'Farmyard Manure'
						else: return 'Farmyard Manure'
					elif obj[3] == '>7.79':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[1] == '>44.8':
					return 'Bone Meal'
				else: return 'Bone Meal'
			else: return 'Farmyard Manure'
		elif obj[7] == '>26.86':
			# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2] == '<=50.0':
				return 'VermiCompost'
			elif obj[2] == '>50.0':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		else: return 'VermiCompost'
	elif obj[16] == ' cotton':
		# {"feature": "Silt %", "instances": 28, "metric_value": 2.7834, "depth": 2}
		if obj[2] == '<=50.0':
			# {"feature": "P ppm", "instances": 27, "metric_value": 2.73, "depth": 3}
			if obj[8] == '<=38.29':
				# {"feature": "Cu ppm", "instances": 26, "metric_value": 2.7037, "depth": 4}
				if obj[14] == '<=2.79':
					# {"feature": "Fe ppm", "instances": 22, "metric_value": 2.7201, "depth": 5}
					if obj[11] == '<=22.65':
						# {"feature": "Mg ppm", "instances": 21, "metric_value": 2.7014, "depth": 6}
						if obj[10] == '<=701':
							# {"feature": "EC mS/cm", "instances": 17, "metric_value": 2.7045, "depth": 7}
							if obj[4] == '>0.321':
								# {"feature": "B ppm", "instances": 16, "metric_value": 2.6556, "depth": 8}
								if obj[15] == '>0.16':
									# {"feature": "CACO3 %", "instances": 12, "metric_value": 2.2842, "depth": 9}
									if obj[6] == '<=28.3':
										# {"feature": "N_NO3 ppm", "instances": 7, "metric_value": 2.5216, "depth": 10}
										if obj[7] == '<=26.86':
											# {"feature": "Zn ppm", "instances": 6, "metric_value": 2.2516, "depth": 11}
											if obj[12] == '<=0.55':
												# {"feature": "pH", "instances": 5, "metric_value": 1.9219, "depth": 12}
												if obj[3] == '<=7.79':
													# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[0] == '>12.0':
														# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[1] == '<=44.8':
															# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[5] == '>0.99':
																# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[9] == '<=551':
																	# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												elif obj[3] == '>7.79':
													# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[0] == '>12.0':
														# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[1] == '<=44.8':
															# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[5] == '>0.99':
																# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9] == '<=551':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											elif obj[12] == '>0.55':
												return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										elif obj[7] == '>26.86':
											return 'Compost'
										else: return 'Compost'
									elif obj[6] == '>28.3':
										# {"feature": "Zn ppm", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[12] == '>0.55':
											return 'Compost'
										elif obj[12] == '<=0.55':
											# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == '>7.79':
												return 'Farmyard Manure'
											elif obj[3] == '<=7.79':
												return 'Compost'
											else: return 'Compost'
										else: return 'Farmyard Manure'
									else: return 'Compost'
								elif obj[15] == '<=0.16':
									# {"feature": "CACO3 %", "instances": 4, "metric_value": 2.0, "depth": 9}
									if obj[6] == '<=28.3':
										# {"feature": "Zn ppm", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[12] == '<=0.55':
											# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[0] == '>12.0':
												# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[1] == '<=44.8':
													# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[3] == '>7.79':
														# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5] == '>0.99':
															# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[7] == '<=26.86':
																# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[9] == '<=551':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										elif obj[12] == '>0.55':
											return 'Composted pine needles'
										else: return 'Composted pine needles'
									elif obj[6] == '>28.3':
										return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'Compost'
							elif obj[4] == '<=0.321':
								return 'Cow Manure'
							else: return 'Cow Manure'
						elif obj[10] == '>701':
							# {"feature": "pH", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[3] == '<=7.79':
								return 'Farmyard Manure'
							elif obj[3] == '>7.79':
								return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'Farmyard Manure'
					elif obj[11] == '>22.65':
						return 'Poultry Manure'
					else: return 'Poultry Manure'
				elif obj[14] == '>2.79':
					# {"feature": "Fe ppm", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[11] == '<=22.65':
						return 'VermiCompost'
					elif obj[11] == '>22.65':
						# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3] == '<=7.79':
							return 'VermiCompost'
						elif obj[3] == '>7.79':
							return 'Green Manure'
						else: return 'Green Manure'
					else: return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[8] == '>38.29':
				return 'Cow Manure'
			else: return 'Cow Manure'
		elif obj[2] == '>50.0':
			return 'Composted pine needles'
		else: return 'Composted pine needles'
	elif obj[16] == ' sugarcane':
		# {"feature": "P ppm", "instances": 24, "metric_value": 2.5528, "depth": 2}
		if obj[8] == '<=38.29':
			# {"feature": "K ppm ", "instances": 23, "metric_value": 2.4031, "depth": 3}
			if obj[9] == '<=551':
				# {"feature": "CACO3 %", "instances": 22, "metric_value": 2.2426, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "N_NO3 ppm", "instances": 21, "metric_value": 2.2244, "depth": 5}
					if obj[7] == '<=26.86':
						# {"feature": "Cu ppm", "instances": 19, "metric_value": 2.1418, "depth": 6}
						if obj[14] == '<=2.79':
							# {"feature": "Zn ppm", "instances": 16, "metric_value": 2.0524, "depth": 7}
							if obj[12] == '<=0.55':
								# {"feature": "Mg ppm", "instances": 13, "metric_value": 1.9878, "depth": 8}
								if obj[10] == '>701':
									# {"feature": "EC mS/cm", "instances": 7, "metric_value": 1.9502, "depth": 9}
									if obj[4] == '>0.321':
										# {"feature": "Fe ppm", "instances": 5, "metric_value": 1.5219, "depth": 10}
										if obj[11] == '>22.65':
											# {"feature": "Clay %", "instances": 4, "metric_value": 1.5, "depth": 11}
											if obj[1] == '>44.8':
												# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[2] == '<=50.0':
														# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[3] == '<=7.79':
															# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[5] == '>0.99':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											elif obj[1] == '<=44.8':
												return 'Green Manure'
											else: return 'Green Manure'
										elif obj[11] == '<=22.65':
											return 'VermiCompost'
										else: return 'VermiCompost'
									elif obj[4] == '<=0.321':
										# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3] == '>7.79':
											return 'Farmyard Manure'
										elif obj[3] == '<=7.79':
											return 'Poultry Manure'
										else: return 'Poultry Manure'
									else: return 'Farmyard Manure'
								elif obj[10] == '<=701':
									# {"feature": "EC mS/cm", "instances": 6, "metric_value": 1.2516, "depth": 9}
									if obj[4] == '>0.321':
										# {"feature": "O.M. %", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "Fe ppm", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[11] == '>22.65':
												# {"feature": "Sand %", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[0] == '>12.0':
													# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[1] == '<=44.8':
														# {"feature": "Silt %", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[2] == '<=50.0':
															# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[3] == '<=7.79':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Farmyard Manure'
																		else: return 'Farmyard Manure'
																	else: return 'Farmyard Manure'
																else: return 'Farmyard Manure'
															else: return 'Farmyard Manure'
														else: return 'Farmyard Manure'
													else: return 'Farmyard Manure'
												else: return 'Farmyard Manure'
											elif obj[11] == '<=22.65':
												return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										elif obj[5] == '<=0.99':
											return 'Farmyard Manure'
										else: return 'Farmyard Manure'
									elif obj[4] == '<=0.321':
										return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'Farmyard Manure'
							elif obj[12] == '>0.55':
								# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4] == '>0.321':
									return 'Compost'
								elif obj[4] == '<=0.321':
									return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							else: return 'Compost'
						elif obj[14] == '>2.79':
							# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1] == '>44.8':
								# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4] == '<=0.321':
									return 'VermiCompost'
								elif obj[4] == '>0.321':
									return 'Poultry Manure'
								else: return 'Poultry Manure'
							elif obj[1] == '<=44.8':
								return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[7] == '>26.86':
						# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1] == '>44.8':
							return 'Poultry Manure'
						elif obj[1] == '<=44.8':
							return 'Green Manure'
						else: return 'Green Manure'
					else: return 'Poultry Manure'
				elif obj[6] == '>28.3':
					return 'Green Manure'
				else: return 'Green Manure'
			elif obj[9] == '>551':
				return 'Bone Meal'
			else: return 'Bone Meal'
		elif obj[8] == '>38.29':
			return 'Wormcasting'
		else: return 'Wormcasting'
	elif obj[16] == ' wheat':
		# {"feature": "O.M. %", "instances": 23, "metric_value": 2.546, "depth": 2}
		if obj[5] == '>0.99':
			# {"feature": "Clay %", "instances": 22, "metric_value": 2.4829, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "B ppm", "instances": 20, "metric_value": 2.3282, "depth": 4}
				if obj[15] == '>0.16':
					# {"feature": "Fe ppm", "instances": 18, "metric_value": 2.288, "depth": 5}
					if obj[11] == '<=22.65':
						# {"feature": "CACO3 %", "instances": 16, "metric_value": 2.3522, "depth": 6}
						if obj[6] == '>28.3':
							# {"feature": "pH", "instances": 9, "metric_value": 1.8366, "depth": 7}
							if obj[3] == '>7.79':
								# {"feature": "EC mS/cm", "instances": 7, "metric_value": 1.3788, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "Sand %", "instances": 6, "metric_value": 1.2516, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "Cu ppm", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[14] == '<=2.79':
											return 'Farmyard Manure'
										elif obj[14] == '>2.79':
											return 'VermiCompost'
										else: return 'VermiCompost'
									elif obj[0] == '<=12.0':
										# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[12] == '>0.55':
											return 'Farmyard Manure'
										elif obj[12] == '<=0.55':
											return 'Compost'
										else: return 'Compost'
									else: return 'Farmyard Manure'
								elif obj[4] == '<=0.321':
									return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[3] == '<=7.79':
								# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[12] == '>0.55':
									return 'Compost'
								elif obj[12] == '<=0.55':
									return 'Chicken Manure'
								else: return 'Chicken Manure'
							else: return 'Compost'
						elif obj[6] == '<=28.3':
							# {"feature": "EC mS/cm", "instances": 7, "metric_value": 2.2359, "depth": 7}
							if obj[4] == '>0.321':
								# {"feature": "Zn ppm", "instances": 6, "metric_value": 1.9183, "depth": 8}
								if obj[12] == '<=0.55':
									# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10] == '>701':
											return 'VermiCompost'
										elif obj[10] == '<=701':
											return 'Farmyard Manure'
										else: return 'Farmyard Manure'
									elif obj[3] == '>7.79':
										return 'Poultry Manure'
									else: return 'Poultry Manure'
								elif obj[12] == '>0.55':
									# {"feature": "Cu ppm", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[14] == '<=2.79':
										# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[0] == '>12.0':
											# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[2] == '<=50.0':
												# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3] == '>7.79':
													# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == '<=38.29':
															# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[10] == '<=701':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									elif obj[14] == '>2.79':
										return 'Green Manure'
									else: return 'Green Manure'
								else: return 'Green Manure'
							elif obj[4] == '<=0.321':
								return 'Compost'
							else: return 'Compost'
						else: return 'VermiCompost'
					elif obj[11] == '>22.65':
						return 'VermiCompost'
					else: return 'VermiCompost'
				elif obj[15] == '<=0.16':
					return 'Green Manure'
				else: return 'Green Manure'
			elif obj[1] == '>44.8':
				# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[11] == '<=22.65':
					return 'Cow Manure'
				elif obj[11] == '>22.65':
					return 'Green Manure'
				else: return 'Green Manure'
			else: return 'Cow Manure'
		elif obj[5] == '<=0.99':
			return 'Chicken Manure'
		else: return 'Chicken Manure'
	elif obj[16] == 'maize':
		# {"feature": "Mg ppm", "instances": 23, "metric_value": 2.1227, "depth": 2}
		if obj[10] == '<=701':
			# {"feature": "O.M. %", "instances": 13, "metric_value": 1.6692, "depth": 3}
			if obj[5] == '>0.99':
				# {"feature": "Fe ppm", "instances": 12, "metric_value": 1.5511, "depth": 4}
				if obj[11] == '<=22.65':
					# {"feature": "P ppm", "instances": 10, "metric_value": 1.2955, "depth": 5}
					if obj[8] == '<=38.29':
						# {"feature": "Mn ppm", "instances": 9, "metric_value": 1.2244, "depth": 6}
						if obj[13] == '<=12.1':
							# {"feature": "CACO3 %", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[6] == '<=28.3':
								# {"feature": "B ppm", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[15] == '>0.16':
									# {"feature": "Zn ppm", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[12] == '<=0.55':
										return 'Farmyard Manure'
									elif obj[12] == '>0.55':
										# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == '<=26.86':
											return 'Compost'
										elif obj[7] == '>26.86':
											return 'Farmyard Manure'
										else: return 'Farmyard Manure'
									else: return 'Compost'
								elif obj[15] == '<=0.16':
									return 'Compost'
								else: return 'Compost'
							elif obj[6] == '>28.3':
								return 'Farmyard Manure'
							else: return 'Farmyard Manure'
						elif obj[13] == '>12.1':
							# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[12] == '>0.55':
								return 'Bone Meal'
							elif obj[12] == '<=0.55':
								return 'Farmyard Manure'
							else: return 'Farmyard Manure'
						else: return 'Bone Meal'
					elif obj[8] == '>38.29':
						return 'Compost'
					else: return 'Compost'
				elif obj[11] == '>22.65':
					# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == '>44.8':
						return 'Farmyard Manure'
					elif obj[1] == '<=44.8':
						return 'VermiCompost'
					else: return 'VermiCompost'
				else: return 'Farmyard Manure'
			elif obj[5] == '<=0.99':
				return 'Bone Meal'
			else: return 'Bone Meal'
		elif obj[10] == '>701':
			# {"feature": "Fe ppm", "instances": 10, "metric_value": 1.6855, "depth": 3}
			if obj[11] == '<=22.65':
				# {"feature": "P ppm", "instances": 5, "metric_value": 1.9219, "depth": 4}
				if obj[8] == '<=38.29':
					# {"feature": "B ppm", "instances": 4, "metric_value": 2.0, "depth": 5}
					if obj[15] == '>0.16':
						# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "EC mS/cm", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[4] == '>0.321':
											# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Zn ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[12] == '<=0.55':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[13] == '<=12.1':
																	# {"feature": "Cu ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						else: return 'Compost'
					elif obj[15] == '<=0.16':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[8] == '>38.29':
					return 'Green Manure'
				else: return 'Green Manure'
			elif obj[11] == '>22.65':
				# {"feature": "Mn ppm", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[13] == '>12.1':
					# {"feature": "Cu ppm", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[14] == '<=2.79':
						# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1] == '>44.8':
							# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == '>0.321':
											# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[8] == '<=38.29':
															# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '<=0.55':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Green Manure'
									else: return 'Green Manure'
								else: return 'Green Manure'
							else: return 'Green Manure'
						elif obj[1] == '<=44.8':
							return 'Bone Meal'
						else: return 'Bone Meal'
					elif obj[14] == '>2.79':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[13] == '<=12.1':
					return 'Green Manure'
				else: return 'Green Manure'
			else: return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == 'mango':
		# {"feature": "Zn ppm", "instances": 22, "metric_value": 2.392, "depth": 2}
		if obj[12] == '>0.55':
			# {"feature": "Silt %", "instances": 18, "metric_value": 2.3936, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "O.M. %", "instances": 17, "metric_value": 2.3243, "depth": 4}
				if obj[5] == '>0.99':
					# {"feature": "Cu ppm", "instances": 16, "metric_value": 2.3522, "depth": 5}
					if obj[14] == '<=2.79':
						# {"feature": "EC mS/cm", "instances": 15, "metric_value": 2.3899, "depth": 6}
						if obj[4] == '<=0.321':
							# {"feature": "Clay %", "instances": 10, "metric_value": 2.171, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Mg ppm", "instances": 8, "metric_value": 1.9056, "depth": 8}
								if obj[10] == '<=701':
									# {"feature": "P ppm", "instances": 4, "metric_value": 1.5, "depth": 9}
									if obj[8] == '<=38.29':
										# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[0] == '>12.0':
											# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Green Manure'
									elif obj[8] == '>38.29':
										return 'Cow Manure'
									else: return 'Cow Manure'
								elif obj[10] == '>701':
									# {"feature": "Sand %", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "pH", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[3] == '<=7.79':
											# {"feature": "CACO3 %", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 4, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "K ppm ", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 4, "metric_value": 1.0, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 4, "metric_value": 1.0, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 4, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 4, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Bone Meal'
																		else: return 'Bone Meal'
																	else: return 'Bone Meal'
																else: return 'Bone Meal'
															else: return 'Bone Meal'
														else: return 'Bone Meal'
													else: return 'Bone Meal'
												else: return 'Bone Meal'
											else: return 'Bone Meal'
										else: return 'Bone Meal'
									else: return 'Bone Meal'
								else: return 'Bone Meal'
							elif obj[1] == '>44.8':
								# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10] == '>701':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												else: return 'Cow Manure'
											else: return 'Cow Manure'
										else: return 'Cow Manure'
									else: return 'Cow Manure'
								else: return 'Cow Manure'
							else: return 'Cow Manure'
						elif obj[4] == '>0.321':
							# {"feature": "Clay %", "instances": 5, "metric_value": 1.9219, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Mg ppm", "instances": 4, "metric_value": 1.5, "depth": 8}
								if obj[10] == '<=701':
									# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[3] == '<=7.79':
											# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								elif obj[10] == '>701':
									return 'Bone Meal'
								else: return 'Bone Meal'
							elif obj[1] == '>44.8':
								return 'Chicken Manure'
							else: return 'Chicken Manure'
						else: return 'Bone Meal'
					elif obj[14] == '>2.79':
						return 'Chicken Manure'
					else: return 'Chicken Manure'
				elif obj[5] == '<=0.99':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[2] == '>50.0':
				return 'Compost'
			else: return 'Compost'
		elif obj[12] == '<=0.55':
			# {"feature": "Mg ppm", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[10] == '>701':
				# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4] == '>0.321':
					return 'Chicken Manure'
				elif obj[4] == '<=0.321':
					return 'Compost'
				else: return 'Compost'
			elif obj[10] == '<=701':
				return 'Compost'
			else: return 'Compost'
		else: return 'Compost'
	elif obj[16] == 'sugar cane':
		# {"feature": "P ppm", "instances": 20, "metric_value": 2.0087, "depth": 2}
		if obj[8] == '<=38.29':
			# {"feature": "EC mS/cm", "instances": 19, "metric_value": 1.9579, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "CACO3 %", "instances": 16, "metric_value": 1.6774, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "B ppm", "instances": 14, "metric_value": 1.5917, "depth": 5}
					if obj[15] == '>0.16':
						# {"feature": "N_NO3 ppm", "instances": 11, "metric_value": 1.3486, "depth": 6}
						if obj[7] == '<=26.86':
							# {"feature": "Mn ppm", "instances": 10, "metric_value": 1.361, "depth": 7}
							if obj[13] == '>12.1':
								# {"feature": "Fe ppm", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[11] == '>22.65':
									# {"feature": "Zn ppm", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[12] == '<=0.55':
										# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1] == '<=44.8':
											# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10] == '<=701':
												return 'Farmyard Manure'
											elif obj[10] == '>701':
												return 'Poultry Manure'
											else: return 'Poultry Manure'
										elif obj[1] == '>44.8':
											return 'Poultry Manure'
										else: return 'Poultry Manure'
									elif obj[12] == '>0.55':
										return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								elif obj[11] == '<=22.65':
									return 'Poultry Manure'
								else: return 'Poultry Manure'
							elif obj[13] == '<=12.1':
								# {"feature": "Zn ppm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12] == '<=0.55':
									return 'Farmyard Manure'
								elif obj[12] == '>0.55':
									return 'Compost'
								else: return 'Compost'
							else: return 'Farmyard Manure'
						elif obj[7] == '>26.86':
							return 'Poultry Manure'
						else: return 'Poultry Manure'
					elif obj[15] == '<=0.16':
						# {"feature": "Mg ppm", "instances": 3, "metric_value": 1.585, "depth": 6}
						if obj[10] == '>701':
							# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[11] == '>22.65':
								return 'VermiCompost'
							elif obj[11] == '<=22.65':
								return 'Poultry Manure'
							else: return 'Poultry Manure'
						elif obj[10] == '<=701':
							return 'Farmyard Manure'
						else: return 'Farmyard Manure'
					else: return 'VermiCompost'
				elif obj[6] == '>28.3':
					# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == '>12.0':
						# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1] == '<=44.8':
							# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == '<=26.86':
											# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9] == '<=551':
												# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[10] == '<=701':
													# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11] == '<=22.65':
														# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12] == '<=0.55':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '<=12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'VermiCompost'
					else: return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[4] == '<=0.321':
				# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 4}
				if obj[5] == '>0.99':
					# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[10] == '<=701':
						return 'Green Manure'
					elif obj[10] == '>701':
						return 'Compost'
					else: return 'Compost'
				elif obj[5] == '<=0.99':
					return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			else: return 'Green Manure'
		elif obj[8] == '>38.29':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == ' turmeric':
		# {"feature": "P ppm", "instances": 18, "metric_value": 2.4613, "depth": 2}
		if obj[8] == '<=38.29':
			# {"feature": "B ppm", "instances": 17, "metric_value": 2.2784, "depth": 3}
			if obj[15] == '>0.16':
				# {"feature": "Fe ppm", "instances": 13, "metric_value": 1.9501, "depth": 4}
				if obj[11] == '<=22.65':
					# {"feature": "N_NO3 ppm", "instances": 11, "metric_value": 1.9363, "depth": 5}
					if obj[7] == '<=26.86':
						# {"feature": "Sand %", "instances": 10, "metric_value": 1.8464, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Mg ppm", "instances": 8, "metric_value": 1.4056, "depth": 7}
							if obj[10] == '<=701':
								# {"feature": "EC mS/cm", "instances": 6, "metric_value": 1.2516, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "Zn ppm", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[12] == '>0.55':
										# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2] == '<=50.0':
											return 'Neem Cake'
										elif obj[2] == '>50.0':
											return 'VermiCompost'
										else: return 'VermiCompost'
									elif obj[12] == '<=0.55':
										return 'VermiCompost'
									else: return 'VermiCompost'
								elif obj[4] == '<=0.321':
									# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == '<=44.8':
										# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5] == '>0.99':
													# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6] == '>28.3':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12] == '<=0.55':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '<=12.1':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[10] == '>701':
								return 'Green Manure'
							else: return 'Green Manure'
						elif obj[0] == '<=12.0':
							# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1] == '>44.8':
								return 'Compost'
							elif obj[1] == '<=44.8':
								return 'Neem Cake'
							else: return 'Neem Cake'
						else: return 'Compost'
					elif obj[7] == '>26.86':
						return 'Compost'
					else: return 'Compost'
				elif obj[11] == '>22.65':
					return 'Compost'
				else: return 'Compost'
			elif obj[15] == '<=0.16':
				# {"feature": "pH", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3] == '>7.79':
					return 'Neem Cake'
				elif obj[3] == '<=7.79':
					return 'Cow Manure'
				else: return 'Cow Manure'
			else: return 'Neem Cake'
		elif obj[8] == '>38.29':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == ' barley':
		# {"feature": "Fe ppm", "instances": 17, "metric_value": 2.8222, "depth": 2}
		if obj[11] == '<=22.65':
			# {"feature": "Mn ppm", "instances": 15, "metric_value": 2.6062, "depth": 3}
			if obj[13] == '<=12.1':
				# {"feature": "B ppm", "instances": 14, "metric_value": 2.4138, "depth": 4}
				if obj[15] == '>0.16':
					# {"feature": "P ppm", "instances": 11, "metric_value": 1.8676, "depth": 5}
					if obj[8] == '<=38.29':
						# {"feature": "CACO3 %", "instances": 9, "metric_value": 1.585, "depth": 6}
						if obj[6] == '<=28.3':
							# {"feature": "Mg ppm", "instances": 7, "metric_value": 1.4488, "depth": 7}
							if obj[10] == '<=701':
								# {"feature": "pH", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3] == '>7.79':
									# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == '<=50.0':
										return 'Compost'
									elif obj[2] == '>50.0':
										return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								elif obj[3] == '<=7.79':
									return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							elif obj[10] == '>701':
								# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1] == '>44.8':
									# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[4] == '>0.321':
													# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5] == '>0.99':
														# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[7] == '<=26.86':
															# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '<=0.55':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								elif obj[1] == '<=44.8':
									return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						elif obj[6] == '>28.3':
							return 'Fish Emulsion'
						else: return 'Fish Emulsion'
					elif obj[8] == '>38.29':
						# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[10] == '<=701':
							return 'Composted pine needles'
						elif obj[10] == '>701':
							return 'Compost'
						else: return 'Compost'
					else: return 'Composted pine needles'
				elif obj[15] == '<=0.16':
					# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3] == '>7.79':
							return 'Composted pine needles'
						elif obj[3] == '<=7.79':
							return 'Bone Meal'
						else: return 'Bone Meal'
					elif obj[1] == '>44.8':
						return 'Cow Manure'
					else: return 'Cow Manure'
				else: return 'Composted pine needles'
			elif obj[13] == '>12.1':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[11] == '>22.65':
			# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4] == '>0.321':
				return 'Green Manure'
			elif obj[4] == '<=0.321':
				return 'Bone Meal'
			else: return 'Bone Meal'
		else: return 'Green Manure'
	elif obj[16] == 'tomato':
		# {"feature": "O.M. %", "instances": 15, "metric_value": 2.3329, "depth": 2}
		if obj[5] == '>0.99':
			# {"feature": "Cu ppm", "instances": 14, "metric_value": 2.121, "depth": 3}
			if obj[14] == '<=2.79':
				# {"feature": "K ppm ", "instances": 13, "metric_value": 1.8843, "depth": 4}
				if obj[9] == '<=551':
					# {"feature": "EC mS/cm", "instances": 12, "metric_value": 1.7842, "depth": 5}
					if obj[4] == '>0.321':
						# {"feature": "Zn ppm", "instances": 6, "metric_value": 1.2516, "depth": 6}
						if obj[12] == '>0.55':
							# {"feature": "Clay %", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Sand %", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "Silt %", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2] == '<=50.0':
										# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3] == '<=7.79':
											# {"feature": "CACO3 %", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "Mg ppm", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[10] == '<=701':
															# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Fish Emulsion'
																		else: return 'Fish Emulsion'
																	else: return 'Fish Emulsion'
																else: return 'Fish Emulsion'
															else: return 'Fish Emulsion'
														else: return 'Fish Emulsion'
													else: return 'Fish Emulsion'
												else: return 'Fish Emulsion'
											else: return 'Fish Emulsion'
										else: return 'Fish Emulsion'
									else: return 'Fish Emulsion'
								else: return 'Fish Emulsion'
							elif obj[1] == '>44.8':
								return 'Fish Emulsion'
							else: return 'Fish Emulsion'
						elif obj[12] == '<=0.55':
							# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1] == '<=44.8':
								return 'Bone Meal'
							elif obj[1] == '>44.8':
								return 'Fish Emulsion'
							else: return 'Fish Emulsion'
						else: return 'Bone Meal'
					elif obj[4] == '<=0.321':
						# {"feature": "Clay %", "instances": 6, "metric_value": 1.4591, "depth": 6}
						if obj[1] == '<=44.8':
							# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.371, "depth": 7}
							if obj[10] == '>701':
								# {"feature": "Zn ppm", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12] == '>0.55':
									# {"feature": "Sand %", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "Silt %", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "CACO3 %", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "P ppm", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == '<=38.29':
															# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Blood Meal'
																		else: return 'Blood Meal'
																	else: return 'Blood Meal'
																else: return 'Blood Meal'
															else: return 'Blood Meal'
														else: return 'Blood Meal'
													else: return 'Blood Meal'
												else: return 'Blood Meal'
											else: return 'Blood Meal'
										else: return 'Blood Meal'
									else: return 'Blood Meal'
								elif obj[12] == '<=0.55':
									return 'Blood Meal'
								else: return 'Blood Meal'
							elif obj[10] == '<=701':
								return 'VermiCompost'
							else: return 'VermiCompost'
						elif obj[1] == '>44.8':
							return 'VermiCompost'
						else: return 'VermiCompost'
					else: return 'Blood Meal'
				elif obj[9] == '>551':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[14] == '>2.79':
				return 'Wormcasting'
			else: return 'Wormcasting'
		elif obj[5] == '<=0.99':
			return 'Chicken Manure'
		else: return 'Chicken Manure'
	elif obj[16] == 'radish':
		# {"feature": "Clay %", "instances": 14, "metric_value": 1.8092, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "N_NO3 ppm", "instances": 11, "metric_value": 1.7899, "depth": 3}
			if obj[7] == '<=26.86':
				# {"feature": "Mg ppm", "instances": 10, "metric_value": 1.761, "depth": 4}
				if obj[10] == '<=701':
					# {"feature": "EC mS/cm", "instances": 6, "metric_value": 1.9183, "depth": 5}
					if obj[4] == '<=0.321':
						# {"feature": "Silt %", "instances": 5, "metric_value": 1.5219, "depth": 6}
						if obj[2] == '<=50.0':
							# {"feature": "Sand %", "instances": 4, "metric_value": 1.5, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "pH", "instances": 4, "metric_value": 1.5, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "O.M. %", "instances": 4, "metric_value": 1.5, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "CACO3 %", "instances": 4, "metric_value": 1.5, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "P ppm", "instances": 4, "metric_value": 1.5, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 4, "metric_value": 1.5, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Fe ppm", "instances": 4, "metric_value": 1.5, "depth": 13}
													if obj[11] == '>22.65':
														# {"feature": "Zn ppm", "instances": 4, "metric_value": 1.5, "depth": 14}
														if obj[12] == '>0.55':
															# {"feature": "Mn ppm", "instances": 4, "metric_value": 1.5, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 4, "metric_value": 1.5, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 4, "metric_value": 1.5, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 4, "metric_value": 1.5, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						elif obj[2] == '>50.0':
							return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[4] == '>0.321':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[10] == '>701':
					# {"feature": "EC mS/cm", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == '<=0.321':
						# {"feature": "Cu ppm", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[14] == '<=2.79':
							# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12] == '>0.55':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							else: return 'VermiCompost'
						elif obj[14] == '>2.79':
							return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[4] == '>0.321':
						return 'VermiCompost'
					else: return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[7] == '>26.86':
				return 'Compost'
			else: return 'Compost'
		elif obj[1] == '>44.8':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == ' chickpeas':
		# {"feature": "Fe ppm", "instances": 14, "metric_value": 2.8424, "depth": 2}
		if obj[11] == '<=22.65':
			# {"feature": "Cu ppm", "instances": 12, "metric_value": 2.4591, "depth": 3}
			if obj[14] == '<=2.79':
				# {"feature": "N_NO3 ppm", "instances": 9, "metric_value": 2.1972, "depth": 4}
				if obj[7] == '<=26.86':
					# {"feature": "pH", "instances": 8, "metric_value": 1.9056, "depth": 5}
					if obj[3] == '>7.79':
						# {"feature": "B ppm", "instances": 5, "metric_value": 1.5219, "depth": 6}
						if obj[15] == '>0.16':
							# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4] == '>0.321':
								# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1] == '<=44.8':
										# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == '>28.3':
													# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[10] == '<=701':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '<=0.55':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							elif obj[4] == '<=0.321':
								return 'VermiCompost'
							else: return 'VermiCompost'
						elif obj[15] == '<=0.16':
							return 'Compost'
						else: return 'Compost'
					elif obj[3] == '<=7.79':
						# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1] == '<=44.8':
							return 'Cow Manure'
						elif obj[1] == '>44.8':
							return 'Compost'
						else: return 'Compost'
					else: return 'Cow Manure'
				elif obj[7] == '>26.86':
					return 'Green Manure'
				else: return 'Green Manure'
			elif obj[14] == '>2.79':
				return 'Composted pine needles'
			else: return 'Composted pine needles'
		elif obj[11] == '>22.65':
			# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == '>44.8':
				return 'Chicken Manure'
			elif obj[1] == '<=44.8':
				return 'Bone Meal'
			else: return 'Bone Meal'
		else: return 'Chicken Manure'
	elif obj[16] == 'turmeric':
		# {"feature": "O.M. %", "instances": 13, "metric_value": 2.0382, "depth": 2}
		if obj[5] == '>0.99':
			# {"feature": "Zn ppm", "instances": 12, "metric_value": 1.9508, "depth": 3}
			if obj[12] == '<=0.55':
				# {"feature": "CACO3 %", "instances": 10, "metric_value": 1.6855, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "Mg ppm", "instances": 8, "metric_value": 1.4056, "depth": 5}
					if obj[10] == '<=701':
						# {"feature": "Mn ppm", "instances": 5, "metric_value": 1.371, "depth": 6}
						if obj[13] == '<=12.1':
							# {"feature": "B ppm", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[15] == '>0.16':
								# {"feature": "Sand %", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[1] == '<=44.8':
										# {"feature": "Silt %", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3] == '<=7.79':
												# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[4] == '>0.321':
													# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "P ppm", "instances": 3, "metric_value": 0.9183, "depth": 14}
														if obj[8] == '<=38.29':
															# {"feature": "K ppm ", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[9] == '<=551':
																# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 16}
																if obj[11] == '<=22.65':
																	# {"feature": "Cu ppm", "instances": 3, "metric_value": 0.9183, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 0.9183, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Farmyard Manure'
																		else: return 'Farmyard Manure'
																	else: return 'Farmyard Manure'
																else: return 'Farmyard Manure'
															else: return 'Farmyard Manure'
														else: return 'Farmyard Manure'
													else: return 'Farmyard Manure'
												else: return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										else: return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							elif obj[15] == '<=0.16':
								return 'Farmyard Manure'
							else: return 'Farmyard Manure'
						elif obj[13] == '>12.1':
							return 'Compost'
						else: return 'Compost'
					elif obj[10] == '>701':
						return 'Compost'
					else: return 'Compost'
				elif obj[6] == '>28.3':
					# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == '>7.79':
						return 'Compost'
					elif obj[3] == '<=7.79':
						return 'Poultry Manure'
					else: return 'Poultry Manure'
				else: return 'Compost'
			elif obj[12] == '>0.55':
				# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == '>7.79':
					return 'Neem Cake'
				elif obj[3] == '<=7.79':
					return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			else: return 'Neem Cake'
		elif obj[5] == '<=0.99':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == ' sorghum':
		# {"feature": "Salinity", "instances": 13, "metric_value": 2.2878, "depth": 2}
		if obj[17] == '>3.9':
			# {"feature": "pH", "instances": 12, "metric_value": 2.0546, "depth": 3}
			if obj[3] == '>7.79':
				# {"feature": "CACO3 %", "instances": 7, "metric_value": 1.3788, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "B ppm", "instances": 6, "metric_value": 1.2516, "depth": 5}
					if obj[15] == '>0.16':
						# {"feature": "Mg ppm", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[10] == '<=701':
							# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1] == '<=44.8':
									# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == '<=50.0':
										# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4] == '>0.321':
											# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '<=22.65':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '<=0.55':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14] == '<=2.79':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						elif obj[10] == '>701':
							return 'Compost'
						else: return 'Compost'
					elif obj[15] == '<=0.16':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4] == '>0.321':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10] == '<=701':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '<=22.65':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '>0.55':
																	# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[13] == '<=12.1':
																		# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[14] == '<=2.79':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						else: return 'Compost'
					else: return 'Compost'
				elif obj[6] == '>28.3':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			elif obj[3] == '<=7.79':
				# {"feature": "CACO3 %", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "EC mS/cm", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == '<=0.321':
						return 'Farmyard Manure'
					elif obj[4] == '>0.321':
						# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[13] == '>12.1':
							return 'Farmyard Manure'
						elif obj[13] == '<=12.1':
							return 'Green Manure'
						else: return 'Green Manure'
					else: return 'Farmyard Manure'
				elif obj[6] == '>28.3':
					return 'Compost'
				else: return 'Compost'
			else: return 'Farmyard Manure'
		elif obj[17] == '<=3.9':
			return 'Blood Meal'
		else: return 'Blood Meal'
	elif obj[16] == 'chillies':
		# {"feature": "pH", "instances": 13, "metric_value": 2.4116, "depth": 2}
		if obj[3] == '<=7.79':
			# {"feature": "P ppm", "instances": 12, "metric_value": 2.1887, "depth": 3}
			if obj[8] == '<=38.29':
				# {"feature": "Cu ppm", "instances": 11, "metric_value": 2.1181, "depth": 4}
				if obj[14] == '<=2.79':
					# {"feature": "Clay %", "instances": 10, "metric_value": 1.8464, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "Mn ppm", "instances": 9, "metric_value": 1.7527, "depth": 6}
						if obj[13] == '>12.1':
							# {"feature": "EC mS/cm", "instances": 8, "metric_value": 1.8113, "depth": 7}
							if obj[4] == '<=0.321':
								# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.5219, "depth": 8}
								if obj[10] == '<=701':
									# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Zn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[12] == '>0.55':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Fish Emulsion'
																		else: return 'Fish Emulsion'
																	else: return 'Fish Emulsion'
																else: return 'Fish Emulsion'
															else: return 'Fish Emulsion'
														else: return 'Fish Emulsion'
													else: return 'Fish Emulsion'
												else: return 'Fish Emulsion'
											else: return 'Fish Emulsion'
										else: return 'Fish Emulsion'
									else: return 'Fish Emulsion'
								elif obj[10] == '>701':
									# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2] == '<=50.0':
											# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5] == '>0.99':
												# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6] == '<=28.3':
													# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7] == '<=26.86':
														# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[12] == '>0.55':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Chicken Manure'
																		else: return 'Chicken Manure'
																	else: return 'Chicken Manure'
																else: return 'Chicken Manure'
															else: return 'Chicken Manure'
														else: return 'Chicken Manure'
													else: return 'Chicken Manure'
												else: return 'Chicken Manure'
											else: return 'Chicken Manure'
										else: return 'Chicken Manure'
									else: return 'Chicken Manure'
								else: return 'Chicken Manure'
							elif obj[4] == '>0.321':
								# {"feature": "Mg ppm", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[10] == '<=701':
									# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[12] == '<=0.55':
										return 'Cow Manure'
									elif obj[12] == '>0.55':
										return 'Bone Meal'
									else: return 'Bone Meal'
								elif obj[10] == '>701':
									return 'Chicken Manure'
								else: return 'Chicken Manure'
							else: return 'Cow Manure'
						elif obj[13] == '<=12.1':
							return 'Cow Manure'
						else: return 'Cow Manure'
					elif obj[1] == '>44.8':
						return 'Bone Meal'
					else: return 'Bone Meal'
				elif obj[14] == '>2.79':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[8] == '>38.29':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[3] == '>7.79':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == 'sweet potato':
		# {"feature": "N_NO3 ppm", "instances": 13, "metric_value": 2.7193, "depth": 2}
		if obj[7] == '<=26.86':
			# {"feature": "Zn ppm", "instances": 12, "metric_value": 2.6887, "depth": 3}
			if obj[12] == '>0.55':
				# {"feature": "Clay %", "instances": 8, "metric_value": 2.25, "depth": 4}
				if obj[1] == '<=44.8':
					# {"feature": "EC mS/cm", "instances": 7, "metric_value": 2.2359, "depth": 5}
					if obj[4] == '<=0.321':
						# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.9219, "depth": 6}
						if obj[10] == '<=701':
							# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "P ppm", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Fe ppm", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												else: return 'Cow Manure'
											else: return 'Cow Manure'
										else: return 'Cow Manure'
									else: return 'Cow Manure'
								else: return 'Cow Manure'
							else: return 'Cow Manure'
						elif obj[10] == '>701':
							# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0] == '>12.0':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Chicken Manure'
																		else: return 'Chicken Manure'
																	else: return 'Chicken Manure'
																else: return 'Chicken Manure'
															else: return 'Chicken Manure'
														else: return 'Chicken Manure'
													else: return 'Chicken Manure'
												else: return 'Chicken Manure'
											else: return 'Chicken Manure'
										else: return 'Chicken Manure'
									else: return 'Chicken Manure'
								else: return 'Chicken Manure'
							else: return 'Chicken Manure'
						else: return 'Chicken Manure'
					elif obj[4] == '>0.321':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10] == '>701':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'VermiCompost'
					else: return 'VermiCompost'
				elif obj[1] == '>44.8':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[12] == '<=0.55':
				# {"feature": "Clay %", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[1] == '>44.8':
					# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0] == '>12.0':
						# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2] == '<=50.0':
							# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4] == '<=0.321':
									# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10] == '>701':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Chicken Manure'
																		else: return 'Chicken Manure'
																	else: return 'Chicken Manure'
																else: return 'Chicken Manure'
															else: return 'Chicken Manure'
														else: return 'Chicken Manure'
													else: return 'Chicken Manure'
												else: return 'Chicken Manure'
											else: return 'Chicken Manure'
										else: return 'Chicken Manure'
									else: return 'Chicken Manure'
								else: return 'Chicken Manure'
							else: return 'Chicken Manure'
						else: return 'Chicken Manure'
					else: return 'Chicken Manure'
				elif obj[1] == '<=44.8':
					# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == '<=0.321':
						return 'Compost'
					elif obj[4] == '>0.321':
						return 'Green Manure'
					else: return 'Green Manure'
				else: return 'Compost'
			else: return 'Green Manure'
		elif obj[7] == '>26.86':
			return 'Compost'
		else: return 'Compost'
	elif obj[16] == 'barley':
		# {"feature": "Clay %", "instances": 12, "metric_value": 2.4591, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "Silt %", "instances": 11, "metric_value": 2.2313, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "CACO3 %", "instances": 10, "metric_value": 2.171, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "Mg ppm", "instances": 8, "metric_value": 2.1556, "depth": 5}
					if obj[10] == '<=701':
						# {"feature": "pH", "instances": 7, "metric_value": 1.8424, "depth": 6}
						if obj[3] == '<=7.79':
							# {"feature": "B ppm", "instances": 4, "metric_value": 1.5, "depth": 7}
							if obj[15] == '>0.16':
								# {"feature": "EC mS/cm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0] == '>12.0':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '<=22.65':
															# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12] == '<=0.55':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '<=12.1':
																	# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[14] == '<=2.79':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Bone Meal'
																		else: return 'Bone Meal'
																	else: return 'Bone Meal'
																else: return 'Bone Meal'
															else: return 'Bone Meal'
														else: return 'Bone Meal'
													else: return 'Bone Meal'
												else: return 'Bone Meal'
											else: return 'Bone Meal'
										else: return 'Bone Meal'
									else: return 'Bone Meal'
								elif obj[4] == '<=0.321':
									return 'Bone Meal'
								else: return 'Bone Meal'
							elif obj[15] == '<=0.16':
								return 'Green Manure'
							else: return 'Green Manure'
						elif obj[3] == '>7.79':
							# {"feature": "B ppm", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[15] == '>0.16':
								return 'Green Manure'
							elif obj[15] == '<=0.16':
								return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'Green Manure'
					elif obj[10] == '>701':
						return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				elif obj[6] == '>28.3':
					return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			elif obj[2] == '>50.0':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		elif obj[1] == '>44.8':
			return 'Compost'
		else: return 'Compost'
	elif obj[16] == 'wheat':
		# {"feature": "Sand %", "instances": 12, "metric_value": 2.2842, "depth": 2}
		if obj[0] == '>12.0':
			# {"feature": "Silt %", "instances": 11, "metric_value": 2.0404, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "Mg ppm", "instances": 10, "metric_value": 1.761, "depth": 4}
				if obj[10] == '<=701':
					# {"feature": "pH", "instances": 7, "metric_value": 1.3788, "depth": 5}
					if obj[3] == '<=7.79':
						# {"feature": "Clay %", "instances": 4, "metric_value": 1.5, "depth": 6}
						if obj[1] == '<=44.8':
							return 'VermiCompost'
						elif obj[1] == '>44.8':
							# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6] == '<=28.3':
								return 'Farmyard Manure'
							elif obj[6] == '>28.3':
								return 'Chicken Manure'
							else: return 'Chicken Manure'
						else: return 'Farmyard Manure'
					elif obj[3] == '>7.79':
						return 'Chicken Manure'
					else: return 'Chicken Manure'
				elif obj[10] == '>701':
					# {"feature": "P ppm", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[8] == '<=38.29':
						# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[14] == '<=2.79':
							return 'Chicken Manure'
						elif obj[14] == '>2.79':
							return 'Cow Manure'
						else: return 'Cow Manure'
					elif obj[8] == '>38.29':
						return 'Cow Manure'
					else: return 'Cow Manure'
				else: return 'Cow Manure'
			elif obj[2] == '>50.0':
				return 'Compost'
			else: return 'Compost'
		elif obj[0] == '<=12.0':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == ' chillies':
		# {"feature": "Zn ppm", "instances": 12, "metric_value": 2.6887, "depth": 2}
		if obj[12] == '>0.55':
			# {"feature": "EC mS/cm", "instances": 9, "metric_value": 1.9749, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "K ppm ", "instances": 7, "metric_value": 1.9502, "depth": 4}
				if obj[9] == '<=551':
					# {"feature": "Clay %", "instances": 6, "metric_value": 1.585, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "CACO3 %", "instances": 5, "metric_value": 1.5219, "depth": 6}
						if obj[6] == '<=28.3':
							# {"feature": "pH", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "P ppm", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[8] == '<=38.29':
									return 'Compost'
								elif obj[8] == '>38.29':
									return 'Cow Manure'
								else: return 'Cow Manure'
							elif obj[3] == '>7.79':
								return 'Cow Manure'
							else: return 'Cow Manure'
						elif obj[6] == '>28.3':
							return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[1] == '>44.8':
						return 'VermiCompost'
					else: return 'VermiCompost'
				elif obj[9] == '>551':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[4] == '<=0.321':
				return 'Bone Meal'
			else: return 'Bone Meal'
		elif obj[12] == '<=0.55':
			# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[1] == '>44.8':
				# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[11] == '<=22.65':
					return 'Composted pine needles'
				elif obj[11] == '>22.65':
					return 'Chicken Manure'
				else: return 'Chicken Manure'
			elif obj[1] == '<=44.8':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		else: return 'Composted pine needles'
	elif obj[16] == ' sunflower':
		# {"feature": "Fe ppm", "instances": 11, "metric_value": 2.7322, "depth": 2}
		if obj[11] == '<=22.65':
			# {"feature": "K ppm ", "instances": 9, "metric_value": 2.281, "depth": 3}
			if obj[9] == '<=551':
				# {"feature": "CACO3 %", "instances": 7, "metric_value": 1.9502, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "EC mS/cm", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[4] == '>0.321':
						# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3] == '>7.79':
							# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[13] == '<=12.1':
								return 'Cow Manure'
							elif obj[13] == '>12.1':
								return 'Poultry Manure'
							else: return 'Poultry Manure'
						elif obj[3] == '<=7.79':
							return 'Poultry Manure'
						else: return 'Poultry Manure'
					elif obj[4] == '<=0.321':
						return 'Compost'
					else: return 'Compost'
				elif obj[6] == '>28.3':
					# {"feature": "Sand %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0] == '<=12.0':
						# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1] == '<=44.8':
							# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3] == '>7.79':
									# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4] == '>0.321':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10] == '<=701':
														# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12] == '>0.55':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '<=12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '>2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'VermiCompost'
																		else: return 'VermiCompost'
																	else: return 'VermiCompost'
																else: return 'VermiCompost'
															else: return 'VermiCompost'
														else: return 'VermiCompost'
													else: return 'VermiCompost'
												else: return 'VermiCompost'
											else: return 'VermiCompost'
										else: return 'VermiCompost'
									else: return 'VermiCompost'
								else: return 'VermiCompost'
							else: return 'VermiCompost'
						else: return 'VermiCompost'
					elif obj[0] == '>12.0':
						return 'VermiCompost'
					else: return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[9] == '>551':
				# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[12] == '>0.55':
					return 'Cow Manure'
				elif obj[12] == '<=0.55':
					return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			else: return 'Cow Manure'
		elif obj[11] == '>22.65':
			# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[10] == '>701':
				return 'Green Manure'
			elif obj[10] == '<=701':
				return 'Blood Meal'
			else: return 'Blood Meal'
		else: return 'Green Manure'
	elif obj[16] == 'sorghum':
		# {"feature": "N_NO3 ppm", "instances": 11, "metric_value": 1.7899, "depth": 2}
		if obj[7] == '<=26.86':
			# {"feature": "Fe ppm", "instances": 10, "metric_value": 1.6855, "depth": 3}
			if obj[11] == '<=22.65':
				# {"feature": "Zn ppm", "instances": 8, "metric_value": 1.4056, "depth": 4}
				if obj[12] == '<=0.55':
					# {"feature": "EC mS/cm", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4] == '>0.321':
						# {"feature": "Clay %", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1] == '<=44.8':
							# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[10] == '<=701':
									return 'Farmyard Manure'
								elif obj[10] == '>701':
									return 'Blood Meal'
								else: return 'Blood Meal'
							elif obj[3] == '>7.79':
								return 'Blood Meal'
							else: return 'Blood Meal'
						elif obj[1] == '>44.8':
							return 'Blood Meal'
						else: return 'Blood Meal'
					elif obj[4] == '<=0.321':
						return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				elif obj[12] == '>0.55':
					# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3] == '>7.79':
							return 'Farmyard Manure'
						elif obj[3] == '<=7.79':
							return 'Green Manure'
						else: return 'Green Manure'
					elif obj[1] == '>44.8':
						return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			elif obj[11] == '>22.65':
				# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == '<=7.79':
					return 'Farmyard Manure'
				elif obj[3] == '>7.79':
					return 'Bone Meal'
				else: return 'Bone Meal'
			else: return 'Farmyard Manure'
		elif obj[7] == '>26.86':
			return 'Bone Meal'
		else: return 'Bone Meal'
	elif obj[16] == ' tomato':
		# {"feature": "Clay %", "instances": 10, "metric_value": 2.9219, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "Mg ppm", "instances": 7, "metric_value": 2.5216, "depth": 3}
			if obj[10] == '<=701':
				# {"feature": "B ppm", "instances": 6, "metric_value": 2.2516, "depth": 4}
				if obj[15] == '>0.16':
					# {"feature": "Fe ppm", "instances": 5, "metric_value": 1.9219, "depth": 5}
					if obj[11] == '>22.65':
						# {"feature": "Sand %", "instances": 3, "metric_value": 1.585, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "EC mS/cm", "instances": 3, "metric_value": 1.585, "depth": 9}
									if obj[4] == '>0.321':
										# {"feature": "O.M. %", "instances": 3, "metric_value": 1.585, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 3, "metric_value": 1.585, "depth": 13}
													if obj[8] == '>38.29':
														# {"feature": "K ppm ", "instances": 3, "metric_value": 1.585, "depth": 14}
														if obj[9] == '<=551':
															# {"feature": "Zn ppm", "instances": 3, "metric_value": 1.585, "depth": 15}
															if obj[12] == '>0.55':
																# {"feature": "Mn ppm", "instances": 3, "metric_value": 1.585, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "Cu ppm", "instances": 3, "metric_value": 1.585, "depth": 17}
																	if obj[14] == '>2.79':
																		# {"feature": "Salinity", "instances": 3, "metric_value": 1.585, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Chicken Manure'
																		else: return 'Chicken Manure'
																	else: return 'Chicken Manure'
																else: return 'Chicken Manure'
															else: return 'Chicken Manure'
														else: return 'Chicken Manure'
													else: return 'Chicken Manure'
												else: return 'Chicken Manure'
											else: return 'Chicken Manure'
										else: return 'Chicken Manure'
									else: return 'Chicken Manure'
								else: return 'Chicken Manure'
							else: return 'Chicken Manure'
						else: return 'Chicken Manure'
					elif obj[11] == '<=22.65':
						# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[8] == '<=38.29':
							return 'VermiCompost'
						elif obj[8] == '>38.29':
							return 'Compost'
						else: return 'Compost'
					else: return 'VermiCompost'
				elif obj[15] == '<=0.16':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[10] == '>701':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[1] == '>44.8':
			# {"feature": "Mg ppm", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[10] == '>701':
				return 'Wormcasting'
			elif obj[10] == '<=701':
				return 'Blood Meal'
			else: return 'Blood Meal'
		else: return 'Wormcasting'
	elif obj[16] == 'potato':
		# {"feature": "K ppm ", "instances": 10, "metric_value": 2.4464, "depth": 2}
		if obj[9] == '<=551':
			# {"feature": "EC mS/cm", "instances": 9, "metric_value": 2.1972, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "Mg ppm", "instances": 5, "metric_value": 1.5219, "depth": 4}
				if obj[10] == '<=701':
					# {"feature": "Zn ppm", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[12] == '>0.55':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						else: return 'Compost'
					elif obj[12] == '<=0.55':
						return 'Bone Meal'
					else: return 'Bone Meal'
				elif obj[10] == '>701':
					# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == '>44.8':
						return 'Compost'
					elif obj[1] == '<=44.8':
						return 'Chicken Manure'
					else: return 'Chicken Manure'
				else: return 'Compost'
			elif obj[4] == '<=0.321':
				# {"feature": "Zn ppm", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[12] == '>0.55':
					# {"feature": "Cu ppm", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[14] == '<=2.79':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1] == '<=44.8':
								# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[2] == '<=50.0':
									# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3] == '<=7.79':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[6] == '<=28.3':
												# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[7] == '<=26.86':
													# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8] == '<=38.29':
														# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[10] == '>701':
															# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[11] == '>22.65':
																# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[13] == '>12.1':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Bone Meal'
																		else: return 'Bone Meal'
																	else: return 'Bone Meal'
																else: return 'Bone Meal'
															else: return 'Bone Meal'
														else: return 'Bone Meal'
													else: return 'Bone Meal'
												else: return 'Bone Meal'
											else: return 'Bone Meal'
										else: return 'Bone Meal'
									else: return 'Bone Meal'
								else: return 'Bone Meal'
							else: return 'Bone Meal'
						else: return 'Bone Meal'
					elif obj[14] == '>2.79':
						return 'VermiCompost'
					else: return 'VermiCompost'
				elif obj[12] == '<=0.55':
					return 'VermiCompost'
				else: return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[9] == '>551':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == ' sesame':
		# {"feature": "Mn ppm", "instances": 9, "metric_value": 2.5033, "depth": 2}
		if obj[13] == '<=12.1':
			# {"feature": "pH", "instances": 7, "metric_value": 1.9502, "depth": 3}
			if obj[3] == '<=7.79':
				# {"feature": "CACO3 %", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4] == '>0.321':
									# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == '<=26.86':
											# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10] == '<=701':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '<=22.65':
															# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[12] == '>0.55':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Cow Manure'
																		else: return 'Cow Manure'
																	else: return 'Cow Manure'
																else: return 'Cow Manure'
															else: return 'Cow Manure'
														else: return 'Cow Manure'
													else: return 'Cow Manure'
												else: return 'Cow Manure'
											else: return 'Cow Manure'
										else: return 'Cow Manure'
									else: return 'Cow Manure'
								else: return 'Cow Manure'
							else: return 'Cow Manure'
						else: return 'Cow Manure'
					elif obj[1] == '>44.8':
						return 'Compost'
					else: return 'Compost'
				elif obj[6] == '>28.3':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			elif obj[3] == '>7.79':
				# {"feature": "K ppm ", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[9] == '<=551':
					return 'VermiCompost'
				elif obj[9] == '>551':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			else: return 'VermiCompost'
		elif obj[13] == '>12.1':
			# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == '<=44.8':
				return 'Bone Meal'
			elif obj[1] == '>44.8':
				return 'Chicken Manure'
			else: return 'Chicken Manure'
		else: return 'Bone Meal'
	elif obj[16] == ' bengalgram':
		# {"feature": "EC mS/cm", "instances": 9, "metric_value": 1.8911, "depth": 2}
		if obj[4] == '>0.321':
			# {"feature": "CACO3 %", "instances": 8, "metric_value": 1.5613, "depth": 3}
			if obj[6] == '<=28.3':
				# {"feature": "Mg ppm", "instances": 6, "metric_value": 1.4591, "depth": 4}
				if obj[10] == '<=701':
					# {"feature": "Clay %", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "pH", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[3] == '<=7.79':
							# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[11] == '<=22.65':
								# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0] == '>12.0':
									# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[2] == '<=50.0':
										# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5] == '>0.99':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12] == '<=0.55':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '<=12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Green Manure'
									else: return 'Green Manure'
								else: return 'Green Manure'
							elif obj[11] == '>22.65':
								return 'Compost'
							else: return 'Compost'
						elif obj[3] == '>7.79':
							return 'Compost'
						else: return 'Compost'
					elif obj[1] == '>44.8':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[10] == '>701':
					return 'Cow Manure'
				else: return 'Cow Manure'
			elif obj[6] == '>28.3':
				return 'Cow Manure'
			else: return 'Cow Manure'
		elif obj[4] == '<=0.321':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == 'sesame':
		# {"feature": "O.M. %", "instances": 9, "metric_value": 2.1972, "depth": 2}
		if obj[5] == '>0.99':
			# {"feature": "Mn ppm", "instances": 8, "metric_value": 1.9056, "depth": 3}
			if obj[13] == '<=12.1':
				# {"feature": "Silt %", "instances": 7, "metric_value": 1.5567, "depth": 4}
				if obj[2] == '<=50.0':
					# {"feature": "Mg ppm", "instances": 6, "metric_value": 1.4591, "depth": 5}
					if obj[10] == '<=701':
						# {"feature": "CACO3 %", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6] == '<=28.3':
							# {"feature": "Salinity", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[17] == '>3.9':
								return 'Poultry Manure'
							elif obj[17] == '<=3.9':
								return 'Compost'
							else: return 'Compost'
						elif obj[6] == '>28.3':
							return 'Compost'
						else: return 'Compost'
					elif obj[10] == '>701':
						return 'Green Manure'
					else: return 'Green Manure'
				elif obj[2] == '>50.0':
					return 'Green Manure'
				else: return 'Green Manure'
			elif obj[13] == '>12.1':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[5] == '<=0.99':
			return 'Neem Cake'
		else: return 'Neem Cake'
	elif obj[16] == ' soybeans':
		# {"feature": "Mn ppm", "instances": 8, "metric_value": 2.5, "depth": 2}
		if obj[13] == '<=12.1':
			# {"feature": "Clay %", "instances": 7, "metric_value": 2.2359, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "Silt %", "instances": 5, "metric_value": 1.9219, "depth": 4}
				if obj[2] == '<=50.0':
					# {"feature": "Mg ppm", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[10] == '<=701':
						# {"feature": "pH", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3] == '>7.79':
							# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6] == '<=28.3':
								return 'Composted pine needles'
							elif obj[6] == '>28.3':
								return 'Green Manure'
							else: return 'Green Manure'
						elif obj[3] == '<=7.79':
							return 'Composted pine needles'
						else: return 'Composted pine needles'
					elif obj[10] == '>701':
						return 'Fish Emulsion'
					else: return 'Fish Emulsion'
				elif obj[2] == '>50.0':
					return 'Compost'
				else: return 'Compost'
			elif obj[1] == '>44.8':
				# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4] == '<=0.321':
					return 'Compost'
				elif obj[4] == '>0.321':
					return 'Wormcasting'
				else: return 'Wormcasting'
			else: return 'Compost'
		elif obj[13] == '>12.1':
			return 'Bone Meal'
		else: return 'Bone Meal'
	elif obj[16] == 'chick peas':
		# {"feature": "EC mS/cm", "instances": 8, "metric_value": 1.9056, "depth": 2}
		if obj[4] == '<=0.321':
			# {"feature": "Clay %", "instances": 6, "metric_value": 1.4591, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "Zn ppm", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[12] == '>0.55':
					# {"feature": "Mg ppm", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[10] == '<=701':
						# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[0] == '>12.0':
							# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2] == '<=50.0':
								# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3] == '<=7.79':
									# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5] == '>0.99':
										# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6] == '<=28.3':
											# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7] == '<=26.86':
												# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[8] == '<=38.29':
													# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[9] == '<=551':
														# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[11] == '>22.65':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '>3.9':
																			return 'Green Manure'
																		else: return 'Green Manure'
																	else: return 'Green Manure'
																else: return 'Green Manure'
															else: return 'Green Manure'
														else: return 'Green Manure'
													else: return 'Green Manure'
												else: return 'Green Manure'
											else: return 'Green Manure'
										else: return 'Green Manure'
									else: return 'Green Manure'
								else: return 'Green Manure'
							else: return 'Green Manure'
						else: return 'Green Manure'
					elif obj[10] == '>701':
						return 'Cow Manure'
					else: return 'Cow Manure'
				elif obj[12] == '<=0.55':
					return 'Cow Manure'
				else: return 'Cow Manure'
			elif obj[1] == '>44.8':
				return 'Green Manure'
			else: return 'Green Manure'
		elif obj[4] == '>0.321':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == ' pearl millet':
		# {"feature": "Silt %", "instances": 7, "metric_value": 2.1281, "depth": 2}
		if obj[2] == '<=50.0':
			# {"feature": "N_NO3 ppm", "instances": 6, "metric_value": 1.7925, "depth": 3}
			if obj[7] == '<=26.86':
				# {"feature": "Mn ppm", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[13] == '<=12.1':
					# {"feature": "B ppm", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[15] == '<=0.16':
						return 'Farmyard Manure'
					elif obj[15] == '>0.16':
						# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6] == '<=28.3':
							return 'Green Manure'
						elif obj[6] == '>28.3':
							return 'Farmyard Manure'
						else: return 'Farmyard Manure'
					else: return 'Green Manure'
				elif obj[13] == '>12.1':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[7] == '>26.86':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[2] == '>50.0':
			return 'Composted pine needles'
		else: return 'Composted pine needles'
	elif obj[16] == ' potato':
		# {"feature": "Silt %", "instances": 7, "metric_value": 1.6645, "depth": 2}
		if obj[2] == '<=50.0':
			# {"feature": "pH", "instances": 6, "metric_value": 1.2516, "depth": 3}
			if obj[3] == '<=7.79':
				# {"feature": "Zn ppm", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[12] == '>0.55':
					return 'Farmyard Manure'
				elif obj[12] == '<=0.55':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[3] == '>7.79':
				return 'Green Manure'
			else: return 'Green Manure'
		elif obj[2] == '>50.0':
			return 'Fish Emulsion'
		else: return 'Fish Emulsion'
	elif obj[16] == 'soy beans':
		# {"feature": "CACO3 %", "instances": 7, "metric_value": 2.2359, "depth": 2}
		if obj[6] == '<=28.3':
			# {"feature": "Clay %", "instances": 6, "metric_value": 1.9183, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "Mg ppm", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[10] == '<=701':
					# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == '>0.321':
						return 'Chicken Manure'
					elif obj[4] == '<=0.321':
						return 'Cow Manure'
					else: return 'Cow Manure'
				elif obj[10] == '>701':
					return 'Compost'
				else: return 'Compost'
			elif obj[1] == '>44.8':
				# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[11] == '>22.65':
					return 'Green Manure'
				elif obj[11] == '<=22.65':
					return 'Cow Manure'
				else: return 'Cow Manure'
			else: return 'Green Manure'
		elif obj[6] == '>28.3':
			return 'Wormcasting'
		else: return 'Wormcasting'
	elif obj[16] == ' cauliflower':
		# {"feature": "Clay %", "instances": 7, "metric_value": 2.5216, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "Mg ppm", "instances": 6, "metric_value": 2.2516, "depth": 3}
			if obj[10] == '<=701':
				# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 4}
				if obj[3] == '>7.79':
					# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[6] == '>28.3':
						return 'Wormcasting'
					elif obj[6] == '<=28.3':
						return 'Fish Emulsion'
					else: return 'Fish Emulsion'
				elif obj[3] == '<=7.79':
					return 'Cow Manure'
				else: return 'Cow Manure'
			elif obj[10] == '>701':
				# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7] == '<=26.86':
					return 'Bone Meal'
				elif obj[7] == '>26.86':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			else: return 'Bone Meal'
		elif obj[1] == '>44.8':
			return 'Compost'
		else: return 'Compost'
	elif obj[16] == ' pigeon peas':
		# {"feature": "EC mS/cm", "instances": 7, "metric_value": 2.2359, "depth": 2}
		if obj[4] == '>0.321':
			# {"feature": "O.M. %", "instances": 6, "metric_value": 1.9183, "depth": 3}
			if obj[5] == '>0.99':
				# {"feature": "CACO3 %", "instances": 5, "metric_value": 1.5219, "depth": 4}
				if obj[6] == '<=28.3':
					# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == '<=44.8':
						return 'VermiCompost'
					elif obj[1] == '>44.8':
						return 'Compost'
					else: return 'Compost'
				elif obj[6] == '>28.3':
					# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == '>7.79':
						return 'Compost'
					elif obj[3] == '<=7.79':
						return 'Bone Meal'
					else: return 'Bone Meal'
				else: return 'Compost'
			elif obj[5] == '<=0.99':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[4] == '<=0.321':
			return 'Chicken Manure'
		else: return 'Chicken Manure'
	elif obj[16] == ' blackgram':
		# {"feature": "CACO3 %", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[6] == '<=28.3':
			return 'VermiCompost'
		elif obj[6] == '>28.3':
			return 'Farmyard Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == 'bottle guard':
		# {"feature": "B ppm", "instances": 6, "metric_value": 1.4591, "depth": 2}
		if obj[15] == '>0.16':
			# {"feature": "Silt %", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "Fe ppm", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[11] == '>22.65':
					# {"feature": "Zn ppm", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[12] == '>0.55':
						return 'Fish Emulsion'
					elif obj[12] == '<=0.55':
						return 'Compost'
					else: return 'Compost'
				elif obj[11] == '<=22.65':
					return 'Compost'
				else: return 'Compost'
			elif obj[2] == '>50.0':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		elif obj[15] == '<=0.16':
			return 'Wormcasting'
		else: return 'Wormcasting'
	elif obj[16] == ' brinjal':
		# {"feature": "Fe ppm", "instances": 6, "metric_value": 1.4591, "depth": 2}
		if obj[11] == '>22.65':
			# {"feature": "EC mS/cm", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[4] == '<=0.321':
				# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[10] == '>701':
					return 'Compost'
				elif obj[10] == '<=701':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[4] == '>0.321':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[11] == '<=22.65':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == ' snake gourd':
		# {"feature": "Clay %", "instances": 5, "metric_value": 1.9219, "depth": 2}
		if obj[1] == '>44.8':
			# {"feature": "K ppm ", "instances": 4, "metric_value": 1.5, "depth": 3}
			if obj[9] == '<=551':
				# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[11] == '<=22.65':
					# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[13] == '<=12.1':
						return 'VermiCompost'
					elif obj[13] == '>12.1':
						return 'Cow Manure'
					else: return 'Cow Manure'
				elif obj[11] == '>22.65':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[9] == '>551':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		elif obj[1] == '<=44.8':
			return 'Compost'
		else: return 'Compost'
	elif obj[16] == ' ginger':
		# {"feature": "Mg ppm", "instances": 5, "metric_value": 2.3219, "depth": 2}
		if obj[10] == '>701':
			# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[12] == '<=0.55':
					return 'Compost'
				elif obj[12] == '>0.55':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[1] == '>44.8':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[10] == '<=701':
			# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4] == '>0.321':
				return 'Farmyard Manure'
			elif obj[4] == '<=0.321':
				return 'Cow Manure'
			else: return 'Cow Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == ' mango':
		# {"feature": "EC mS/cm", "instances": 5, "metric_value": 1.9219, "depth": 2}
		if obj[4] == '>0.321':
			# {"feature": "Mg ppm", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[10] == '<=701':
				# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == '>12.0':
					# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2] == '<=50.0':
							# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5] == '>0.99':
									# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6] == '<=28.3':
										# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == '<=26.86':
											# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11] == '>22.65':
														# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12] == '>0.55':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Farmyard Manure'
																		else: return 'Farmyard Manure'
																	else: return 'Farmyard Manure'
																else: return 'Farmyard Manure'
															else: return 'Farmyard Manure'
														else: return 'Farmyard Manure'
													else: return 'Farmyard Manure'
												else: return 'Farmyard Manure'
											else: return 'Farmyard Manure'
										else: return 'Farmyard Manure'
									else: return 'Farmyard Manure'
								else: return 'Farmyard Manure'
							else: return 'Farmyard Manure'
						else: return 'Farmyard Manure'
					else: return 'Farmyard Manure'
				else: return 'Farmyard Manure'
			elif obj[10] == '>701':
				return 'Cow Manure'
			else: return 'Cow Manure'
		elif obj[4] == '<=0.321':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == ' cabbage':
		# {"feature": "Fe ppm", "instances": 5, "metric_value": 2.3219, "depth": 2}
		if obj[11] == '>22.65':
			# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[1] == '<=44.8':
				# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[12] == '<=0.55':
					return 'Compost'
				elif obj[12] == '>0.55':
					return 'Bone Meal'
				else: return 'Bone Meal'
			elif obj[1] == '>44.8':
				return 'Blood Meal'
			else: return 'Blood Meal'
		elif obj[11] == '<=22.65':
			# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[15] == '<=0.16':
				return 'Wormcasting'
			elif obj[15] == '>0.16':
				return 'VermiCompost'
			else: return 'VermiCompost'
		else: return 'Wormcasting'
	elif obj[16] == 'green peas':
		# {"feature": "Fe ppm", "instances": 5, "metric_value": 2.3219, "depth": 2}
		if obj[11] == '>22.65':
			# {"feature": "EC mS/cm", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "Sand %", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == '>12.0':
					# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == '<=44.8':
						# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2] == '<=50.0':
							# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3] == '<=7.79':
								# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5] == '>0.99':
									# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[6] == '<=28.3':
										# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7] == '<=26.86':
											# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[8] == '<=38.29':
												# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[9] == '<=551':
													# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[10] == '<=701':
														# {"feature": "Zn ppm", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12] == '<=0.55':
															# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 15}
															if obj[13] == '>12.1':
																# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 16}
																if obj[14] == '<=2.79':
																	# {"feature": "B ppm", "instances": 2, "metric_value": 1.0, "depth": 17}
																	if obj[15] == '>0.16':
																		# {"feature": "Salinity", "instances": 2, "metric_value": 1.0, "depth": 18}
																		if obj[17] == '<=3.9':
																			return 'Compost'
																		else: return 'Compost'
																	else: return 'Compost'
																else: return 'Compost'
															else: return 'Compost'
														else: return 'Compost'
													else: return 'Compost'
												else: return 'Compost'
											else: return 'Compost'
										else: return 'Compost'
									else: return 'Compost'
								else: return 'Compost'
							else: return 'Compost'
						else: return 'Compost'
					else: return 'Compost'
				else: return 'Compost'
			elif obj[4] == '<=0.321':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[11] == '<=22.65':
			# {"feature": "K ppm ", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[9] == '<=551':
				return 'Blood Meal'
			elif obj[9] == '>551':
				return 'Bone Meal'
			else: return 'Bone Meal'
		else: return 'Blood Meal'
	elif obj[16] == ' bittergourd':
		# {"feature": "EC mS/cm", "instances": 4, "metric_value": 1.5, "depth": 2}
		if obj[4] == '>0.321':
			# {"feature": "Fe ppm", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[11] == '<=22.65':
				return 'Green Manure'
			elif obj[11] == '>22.65':
				return 'Poultry Manure'
			else: return 'Poultry Manure'
		elif obj[4] == '<=0.321':
			return 'Farmyard Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == ' greenpeas':
		# {"feature": "pH", "instances": 4, "metric_value": 2.0, "depth": 2}
		if obj[3] == '>7.79':
			# {"feature": "EC mS/cm", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[4] == '>0.321':
				# {"feature": "CACO3 %", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[6] == '>28.3':
					return 'Fish Emulsion'
				elif obj[6] == '<=28.3':
					return 'Chicken Manure'
				else: return 'Chicken Manure'
			elif obj[4] == '<=0.321':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[3] == '<=7.79':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == ' redgram':
		# {"feature": "Fe ppm", "instances": 4, "metric_value": 1.5, "depth": 2}
		if obj[11] == '>22.65':
			# {"feature": "N_NO3 ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[7] == '>26.86':
				return 'Farmyard Manure'
			elif obj[7] == '<=26.86':
				return 'Neem Cake'
			else: return 'Neem Cake'
		elif obj[11] == '<=22.65':
			# {"feature": "pH", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3] == '<=7.79':
				return 'VermiCompost'
			elif obj[3] == '>7.79':
				return 'Farmyard Manure'
			else: return 'Farmyard Manure'
		else: return 'VermiCompost'
	elif obj[16] == ' Cabbage':
		# {"feature": "Clay %", "instances": 4, "metric_value": 2.0, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "CACO3 %", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[6] == '<=28.3':
				# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[8] == '>38.29':
					return 'Green Manure'
				elif obj[8] == '<=38.29':
					return 'Fish Emulsion'
				else: return 'Fish Emulsion'
			elif obj[6] == '>28.3':
				return 'Compost'
			else: return 'Compost'
		elif obj[1] == '>44.8':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == 'carrot':
		# {"feature": "Cu ppm", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[14] == '<=2.79':
			return 'Bone Meal'
		elif obj[14] == '>2.79':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == 'ginger':
		# {"feature": "Clay %", "instances": 4, "metric_value": 1.5, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[7] == '<=26.86':
				# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[13] == '>12.1':
					return 'Cow Manure'
				elif obj[13] == '<=12.1':
					return 'VermiCompost'
				else: return 'VermiCompost'
			elif obj[7] == '>26.86':
				return 'VermiCompost'
			else: return 'VermiCompost'
		elif obj[1] == '>44.8':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == ' mustard':
		# {"feature": "Clay %", "instances": 4, "metric_value": 2.0, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "Silt %", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[2] == '<=50.0':
				# {"feature": "Fe ppm", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[11] == '>22.65':
					return 'VermiCompost'
				elif obj[11] == '<=22.65':
					return 'Poultry Manure'
				else: return 'Poultry Manure'
			elif obj[2] == '>50.0':
				return 'Farmyard Manure'
			else: return 'Farmyard Manure'
		elif obj[1] == '>44.8':
			return 'Bone Meal'
		else: return 'Bone Meal'
	elif obj[16] == 'mustard':
		# {"feature": "EC mS/cm", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[4] == '<=0.321':
			# {"feature": "P ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[8] == '>38.29':
				return 'Poultry Manure'
			elif obj[8] == '<=38.29':
				return 'Green Manure'
			else: return 'Green Manure'
		elif obj[4] == '>0.321':
			return 'Bone Meal'
		else: return 'Bone Meal'
	elif obj[16] == 'pearl millet':
		# {"feature": "Clay %", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == '<=44.8':
			return 'Bone Meal'
		elif obj[1] == '>44.8':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == ' bottlegourd':
		# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4] == '<=0.321':
				return 'VermiCompost'
			elif obj[4] == '>0.321':
				return 'Wormcasting'
			else: return 'Wormcasting'
		elif obj[1] == '>44.8':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == 'cabbage':
		# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[7] == '<=26.86':
			# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[10] == '<=701':
				return 'Poultry Manure'
			elif obj[10] == '>701':
				return 'Cow Manure'
			else: return 'Cow Manure'
		elif obj[7] == '>26.86':
			return 'Green Manure'
		else: return 'Green Manure'
	elif obj[16] == 'red gram':
		# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[7] == '<=26.86':
			# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[10] == '>701':
				return 'Compost'
			elif obj[10] == '<=701':
				return 'Green Manure'
			else: return 'Green Manure'
		elif obj[7] == '>26.86':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == ' ridge gourd':
		# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "Cu ppm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[14] == '<=2.79':
				return 'Compost'
			elif obj[14] == '>2.79':
				return 'Fish Emulsion'
			else: return 'Fish Emulsion'
		elif obj[1] == '>44.8':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == ' carrot':
		# {"feature": "N_NO3 ppm", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[7] == '<=26.86':
			return 'Bone Meal'
		elif obj[7] == '>26.86':
			return 'Compost'
		else: return 'Compost'
	elif obj[16] == ' castor':
		# {"feature": "Clay %", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[1] == '<=44.8':
			# {"feature": "O.M. %", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[5] == '<=0.99':
				return 'Bone Meal'
			elif obj[5] == '>0.99':
				return 'Farmyard Manure'
			else: return 'Farmyard Manure'
		elif obj[1] == '>44.8':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == ' maize ':
		# {"feature": "pH", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[3] == '>7.79':
			# {"feature": "EC mS/cm", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4] == '<=0.321':
				return 'VermiCompost'
			elif obj[4] == '>0.321':
				return 'Compost'
			else: return 'Compost'
		elif obj[3] == '<=7.79':
			return 'Farmyard Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == 'bengal gram':
		# {"feature": "Mg ppm", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[10] == '<=701':
			return 'Green Manure'
		elif obj[10] == '>701':
			return 'VermiCompost'
		else: return 'VermiCompost'
	elif obj[16] == 'bitter guard':
		return 'Wormcasting'
	elif obj[16] == 'snake guard':
		# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '>44.8':
			return 'Chicken Manure'
		elif obj[1] == '<=44.8':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == 'cauli flower':
		# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '>44.8':
			return 'Wormcasting'
		elif obj[1] == '<=44.8':
			return 'Bone Meal'
		else: return 'Bone Meal'
	elif obj[16] == 'Chick peas':
		# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '<=44.8':
			return 'Poultry Manure'
		elif obj[1] == '>44.8':
			return 'Farmyard Manure'
		else: return 'Farmyard Manure'
	elif obj[16] == 'Barley':
		# {"feature": "Silt %", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[2] == '<=50.0':
			return 'Cow Manure'
		elif obj[2] == '>50.0':
			return 'Poultry Manure'
		else: return 'Poultry Manure'
	elif obj[16] == 'pintobeans':
		# {"feature": "Mn ppm", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[13] == '>12.1':
			return 'Chicken Manure'
		elif obj[13] == '<=12.1':
			return 'Cow Manure'
		else: return 'Cow Manure'
	elif obj[16] == ' barley ':
		# {"feature": "Clay %", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == '<=44.8':
			return 'Compost'
		elif obj[1] == '>44.8':
			return 'Fish Emulsion'
		else: return 'Fish Emulsion'
	elif obj[16] == ' Sorghum':
		return 'Poultry Manure'
	elif obj[16] == ' chillies ':
		return 'Farmyard Manure'
	elif obj[16] == 'sugarcane':
		return 'VermiCompost'
	elif obj[16] == 'bottle gourd':
		return 'Compost'
	elif obj[16] == 'sweat pea':
		return 'Cow Manure'
	elif obj[16] == ' kidneybean':
		return 'Cow Manure'
	elif obj[16] == 'black gram':
		return 'Compost'
	elif obj[16] == 'kidneybeans':
		return 'Cow Manure'
	elif obj[16] == ' watermelon':
		return 'VermiCompost'
	elif obj[16] == 'sunflower':
		return 'Composted pine needles'
	elif obj[16] == ' pintobeans':
		return 'Green Manure'
	elif obj[16] == ' raddish':
		return 'Composted pine needles'
	elif obj[16] == ' Maize':
		return 'Cow Manure'
	elif obj[16] == 'cauliflower':
		return 'Bone Meal'
	elif obj[16] == ' wheat ':
		return 'Chicken Manure'
	elif obj[16] == ' sorgham ':
		return 'Farmyard Manure'
	elif obj[16] == ' potato ':
		return 'Bone Meal'
	elif obj[16] == ' sorghum ':
		return 'Blood Meal'
	elif obj[16] == ' cotton  ':
		return 'Green Manure'
	elif obj[16] == ' brinjal ':
		return 'Cow Manure'
	elif obj[16] == ' sesame ':
		return 'Green Manure'
	elif obj[16] == ' mango ':
		return 'Bone Meal'
	elif obj[16] == 'watermelon':
		return 'VermiCompost'
	elif obj[16] == ' tomato ':
		return 'Wormcasting'
	elif obj[16] == ' sugarcane ':
		return 'Compost'
	elif obj[16] == 'sweet peas':
		return 'Fish Emulsion'
	else: return 'Fish Emulsion'
