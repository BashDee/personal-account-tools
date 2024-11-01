from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AssetModel(BaseModel):
    id: int
    name: str
    value: float
    is_liquid: bool

class Assets:
    """Assets class to add asset, remove and modify assets"""
    def __init__(self):
        self.assets = {}

    def add_asset(self, user, asset: AssetModel):
        """This method adds an asset"""
        if id in self.assets:
            print(f"{id}: Already exist")
        self.assets[asset.id] = {'name': asset.name, 'value': asset.value, 'is_liquid': asset.is_liquid}

    def remove_asset(self, user, id: int):
        if id in self.assets:
            removed_asset = self.assets.pop(id)
            return removed_asset
        else:
            raise HTTPException(status_code=404, detail="Asset not found")

    def modify_asset(self, user, id: int, name: str = None, value: float = None):
        if id in self.assets:
            if name:
                self.assets[id]['name'] = name
            if value:
                self.assets[id]['value'] = value
            return self.assets[id]
        else:
            raise HTTPException(status_code=404, detail="Asset not found")

    def list_assets(self, user, assets: AssetModel):
        return self.assets

    def total_assets_value(self):
        total_value = sum(asset['value'] for asset in self.assets.values())
        return total_value

my_assets = Assets()

@app.post("/add_asset/")
def add_asset(user: str, asset: AssetModel):
    my_assets.add_asset(user, asset)
    return {"message": "Asset added"}

@app.delete("/remove_asset/{id}")
def remove_asset(user: str, id: int):
    removed_asset = my_assets.remove_asset(user, id)
    return {"message": f"Asset removed: {removed_asset}"}

@app.put("/modify_asset/{id}")
def modify_asset(user: str, id: int, name: str = None, value: float = None):
    modified_asset = my_assets.modify_asset(user, id, name, value)
    return {"message": "Asset modified", "asset": modified_asset}

@app.get("/list_assets")
def list_assets(user: str):
    assets = my_assets.list_assets(user)
    return {"assets": assets}

@app.get("/total_value/")
def total_value():
    total = my_assets.total_assets_value()
    return {"total_value": total}
