import json
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

with open("menu.json", "r") as read_file: 
    data = json.load(read_file)
app = FastAPI() 

@app.get('/')
def root():
    return{'Menu':'Item'}

@app.get('/menu') 
async def read_all_menu(): 
    return data

@app.get('/menu/{item_id}') 
async def read_menu(item_id: int): 
	for menu_item in data['menu']:
		if menu_item['id'] == item_id:
			return menu_item
	raise HTTPException( # Membuat Excpetion Handling
			status_code = 404, detail = f'Item not found!'
		)

@app.post('/menu')
async def post_menu(name:str):
    id=1 #initial id
    if(len(data['menu'])>0): #cek supaya id yg ditambah adalah id terakhir+1
        id=data['menu'][len(data['menu'])-1]['id']+1 
    data_tambah={'id':id, 'name':name}
    #dilakukan append penambahan data_tambah pada data menu
	data['menu'].append(dict(data_tambah))
	read_file.close()
	with open("menu.json","w") as write_file:
		json.dump(data,write_file,indent = 4)
	write.file.close()
    
    return(data_tambah)
    
    raise HTTPException( #membuat exception handling
        status_code=500, detail=f'Internal Server Error'
    )


@app.put('/menu/{item_id}') 
async def update_menu(item_id: int, name:str): 
	for menu_item in data['menu']:
		if menu_item['id'] == item_id:
			menu_item['name'] = name
			read_file.close()
			with open("menu.json","w") as write_file:
				json.dump(data,write_file,indent = 4)
			write.file.close()

			return("message : Data updated!") # return pesan data terupdate

    raise HTTPException( #membuat exception handling
        status_code=404, detail=f'Item not found'
        )

@app.delete('/menu/{item_id}') 
async def delete_menu(item_id: int): 
	for menu_item in data['menu']:
		if menu_item['id'] == item_id:
			data['menu'].remove(menu_item)
			read_file.close()
			with open("menu.json","w") as write_file:
				json.dump(data,write_file,indent = 4) 
			write.file.close()

			return("message : Data deleted!") # return pesan data terhapus
            
    raise HTTPException( #membuat exception handling
        status_code=404, detail=f'Item not found'
        )