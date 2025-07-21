# Overview (list of industries and cargos)

## Industries

The set contains 20 industries as listed below.

### Builders yard

<img src="builders_yard.png" alt="Builders yard">

Description to go here

| Requires | Produces |
| -- | -- |
| [Timber](#timber) |  |

### Coal mine

<img src="coal_mine.png" alt="Coal mine">

Description to go here

Industry will only spawn from 1800 to 1950.
This restriction is also valid for funding the industry.
| Requires | Produces |
| -- | -- |
|  | [Coal](#coal) |

### Department store

<img src="department_store.png" alt="Department store">

Description to go here

| Requires | Produces |
| -- | -- |
| [Goods](#goods) |  |

### Farm

<img src="farm.png" alt="Farm">

Description to go here

| Requires | Produces |
| -- | -- |
|  | [Grain](#grain) |
|  | [Livestock](#livestock) |

### Fishing grounds

<img src="fishing_grounds.png" alt="Fishing grounds">

Description to go here

| Requires | Produces |
| -- | -- |
|  | [Fish](#fish) |

### Food processor

<img src="food_processor.png" alt="Food processor">

Description to go here

| Requires | Produces |
| -- | -- |
| [Fish](#fish) | [Food](#food) |
| [Grain](#grain) |  |
| [Livestock](#livestock) |  |

### Forest

<img src="forest.png" alt="Forest">

Description to go here

| Requires | Produces |
| -- | -- |
|  | [Wood](#wood) |

### Furniture factory

<img src="furniture_factory.png" alt="Furniture factory">

Description to go here

| Requires | Produces |
| -- | -- |
| [Timber](#timber) | [Goods](#goods) |

### General store

<img src="general_store.png" alt="General store">

Description to go here

| Requires | Produces |
| -- | -- |
| [Food](#food) |  |

### Hotel

<img src="hotel.png" alt="Hotel">

Description to go here

| Requires | Produces |
| -- | -- |
| [Food](#food) | [Passengers](#passengers) |
| [Passengers](#passengers) |  |

### Integrated steel mill

<img src="integrated_steel_mill.png" alt="Integrated steel mill">

Description to go here

| Requires | Produces |
| -- | -- |
| [Coal](#coal) | [Steel](#steel) |
| [Iron Ore](#iron-ore) |  |

### Iron ore mine

<img src="iron_ore_mine.png" alt="Iron ore mine">

Description to go here

| Requires | Produces |
| -- | -- |
|  | [Iron Ore](#iron-ore) |

### Oil refinery

<img src="oil_refinery.png" alt="Oil refinery">

Description to go here

Industry will only spawn after 1860.
This restriction is also valid for funding the industry.
| Requires | Produces |
| -- | -- |
| [Oil](#oil) | [Plastics](#plastics) |

### Oil rig

<img src="oil_rig.png" alt="Oil rig">

Description to go here

Industry will only spawn after 1985.
This restriction is also valid for funding the industry.
| Requires | Produces |
| -- | -- |
| [Passengers](#passengers) | [Oil](#oil) |
|  | [Passengers](#passengers) |

### Oil well

<img src="oil_well.png" alt="Oil well">

Description to go here

Industry will only spawn from 1860 to 1985.
This restriction is also valid for funding the industry.
| Requires | Produces |
| -- | -- |
|  | [Oil](#oil) |
|  | [Passengers](#passengers) |

### Port

<img src="port.png" alt="Port">

Description to go here

| Requires | Produces |
| -- | -- |
| [Goods](#goods) | [Coal](#coal) |
| [Vehicles](#vehicles) | [Iron Ore](#iron-ore) |
|  | [Oil](#oil) |

### Power plant

<img src="power_plant.png" alt="Power plant">

Description to go here

| Requires | Produces |
| -- | -- |
| [Coal](#coal) | [Electricity](#electricity) |
| [Oil](#oil) |  |

### Sawmill

<img src="sawmill.png" alt="Sawmill">

Description to go here

| Requires | Produces |
| -- | -- |
| [Wood](#wood) | [Timber](#timber) |

### Vehicle distributor

<img src="vehicle_distributor.png" alt="Vehicle distributor">

Description to go here

| Requires | Produces |
| -- | -- |
| [Vehicles](#vehicles) |  |

### Vehicle factory

<img src="vehicle_factory.png" alt="Vehicle factory">

blabla

Industry will only spawn after 1910.
This restriction is also valid for funding the industry.
| Requires | Produces |
| -- | -- |
| [Electricity](#electricity) | [Vehicles](#vehicles) |
| [Steel](#steel) |  |

## Cargos

The set contains 16 cargos as listed below.

### Coal

no description yet

Cargo classes: Bulk cargo
| Produced by | Required by |
| -- | -- |
| [Coal mine](#coal-mine) | [Integrated steel mill](#integrated-steel-mill) |
| [Port](#port) | [Power plant](#power-plant) |

### Electricity

no description yet

| Produced by | Required by |
| -- | -- |
| [Power plant](#power-plant) | [Vehicle factory](#vehicle-factory) |

### Fish

no description yet

Cargo classes: Express, Refrigerated
| Produced by | Required by |
| -- | -- |
| [Fishing grounds](#fishing-grounds) | [Food processor](#food-processor) |

### Food

no description yet

Cargo classes: Express, Refrigerated
| Produced by | Required by |
| -- | -- |
| [Food processor](#food-processor) | [General store](#general-store) |
|  | [Hotel](#hotel) |

### Goods

no description yet

Cargo classes: Express
| Produced by | Required by |
| -- | -- |
| [Furniture factory](#furniture-factory) | [Department store](#department-store) |
|  | [Port](#port) |

### Grain

no description yet

Cargo classes: Bulk cargo
| Produced by | Required by |
| -- | -- |
| [Farm](#farm) | [Food processor](#food-processor) |

### Iron Ore

no description yet

Cargo classes: Bulk cargo
| Produced by | Required by |
| -- | -- |
| [Iron ore mine](#iron-ore-mine) | [Integrated steel mill](#integrated-steel-mill) |
| [Port](#port) |  |

### Livestock

no description yet

Cargo classes: Piece goods
| Produced by | Required by |
| -- | -- |
| [Farm](#farm) | [Food processor](#food-processor) |

### Mail

no description yet

Cargo classes: Mail
| Produced by | Required by |
| -- | -- |

### Oil

no description yet

Cargo classes: Liquid
| Produced by | Required by |
| -- | -- |
| [Oil rig](#oil-rig) | [Oil refinery](#oil-refinery) |
| [Oil well](#oil-well) | [Power plant](#power-plant) |
| [Port](#port) |  |

### Passengers

no description yet

Cargo classes: Passengers
| Produced by | Required by |
| -- | -- |
| [Hotel](#hotel) | [Hotel](#hotel) |
| [Oil rig](#oil-rig) | [Oil rig](#oil-rig) |
| [Oil well](#oil-well) |  |

### Plastics

no description yet

Cargo classes: Bulk cargo, Piece goods
| Produced by | Required by |
| -- | -- |
| [Oil refinery](#oil-refinery) |  |

### Steel

no description yet

Cargo classes: Piece goods
| Produced by | Required by |
| -- | -- |
| [Integrated steel mill](#integrated-steel-mill) | [Vehicle factory](#vehicle-factory) |

### Timber

no description yet

Cargo classes: Piece goods
| Produced by | Required by |
| -- | -- |
| [Sawmill](#sawmill) | [Builders yard](#builders-yard) |
|  | [Furniture factory](#furniture-factory) |

### Vehicles

no description yet

Cargo classes: Oversized, Piece goods
| Produced by | Required by |
| -- | -- |
| [Vehicle factory](#vehicle-factory) | [Port](#port) |
|  | [Vehicle distributor](#vehicle-distributor) |

### Wood

no description yet

Cargo classes: Piece goods
| Produced by | Required by |
| -- | -- |
| [Forest](#forest) | [Sawmill](#sawmill) |

