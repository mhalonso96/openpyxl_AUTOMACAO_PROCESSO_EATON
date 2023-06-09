# data = 'TOX // 8455.22 // 07/06/23 // MANGUEIRA ORC 326971 // 1 // 019861 // LINHA GVV // FLVV10 // BAIXO // 63303 // 25215 // 270340 // 30/07/23 // ADRIEL // BOTELHO // PREVISAO AGOSTO'
# teste = data.split(' // ')
def data_filter_sheet(data, max_column):
        try:
                data_index = data.split(' // ')
                #print('data:',data_index)
                #print('tamanho', len(data_index))
                new_data=[]
                index = max_column 
                if index == 21:    
                        for item in range(0,index):
                                if item == 0: 
                                        new_data.insert(0,None)
                                if item == 1: 
                                        new_data.insert(1,'c')
                                if item == 2: 
                                        new_data.append(str(data_index[0]))      
                                if item == 3: 
                                        new_data.append(float(data_index[1]))  
                                if item == 4: 
                                        new_data.append(str(data_index[2]))  
                                if item == 5: 
                                        new_data.append(str(data_index[3]))  
                                if item == 6: 
                                        new_data.append(str(data_index[4])) 
                                if item == 7: 
                                        new_data.insert(7,None)
                                if item == 8: 
                                        new_data.append(int(data_index[5])) 
                                if item == 9: 
                                        new_data.append(str(data_index[6]))
                                if item == 10: 
                                        new_data.append(str(data_index[7]))  
                                if item == 11: 
                                        new_data.append(str(data_index[8])) 
                                if item == 12: 
                                        new_data.append(str(data_index[9]))
                                if item == 13: 
                                        new_data.append(int(data_index[10]))
                                if item == 14: 
                                        new_data.insert(14,None)
                                if item == 15: 
                                        new_data.insert(15,None)
                                if item == 16: 
                                        new_data.append(int(data_index[11]))
                                if item == 17: 
                                        new_data.append(str(data_index[12])) 
                                if item == 18: 
                                        new_data.append(str(data_index[13])) 
                                if item == 19: 
                                        new_data.append(str(data_index[14]))  
                                if item == 20:
                                        new_data.append(str(data_index[15]))
                        #print('new_data', new_data)        
                        return new_data         
                else:
                        raise Exception 
        
        except Exception as error:
                return error
                                                        