#!/usr/bin/env python
# coding: utf-8

# # Water Quality Simulation
# 
# ## Water Quality Measures
# There are several common (legacy) measures of water quality, including:
# 
# - pH: This measures the acidity or alkalinity of the water. The pH scale ranges from 0 to 14, with 7 being neutral. pH is important because it can affect the solubility of minerals in the water, which in turn can impact the health of aquatic organisms.
# 
# - Dissolved Oxygen (DO): This measures the amount of oxygen dissolved in the water. DO is important for aquatic organisms to survive, as they need oxygen to breathe. Low levels of DO can indicate pollution or other environmental problems.
# 
# - Turbidity: This measures the amount of suspended particles in the water. Turbidity can impact water quality because it can affect the ability of light to penetrate the water, which in turn can impact aquatic plants and animals.
# 
# - Total Dissolved Solids (TDS): This measures the amount of dissolved solids, such as minerals, salts, and metals, in the water. High levels of TDS can indicate pollution and can affect the taste and smell of drinking water.
# 
# - Biochemical Oxygen Demand (BOD): This measures the amount of oxygen required by microorganisms to break down organic matter in the water. High levels of BOD can indicate pollution and can lead to oxygen depletion in the water, which can harm aquatic organisms.
# 
# These measures are important because they help us understand the health of aquatic ecosystems, as well as the safety and suitability of water for drinking, recreation, and other uses. By monitoring these measures, we can identify environmental problems and take action to protect and improve water quality.
# 
# The list above are important traditional (legacy) metrics of water quality; there are also newer and emerging measures that have gained importance in recent years. Some of these include:
# 
# - Microplastics: This refers to tiny pieces of plastic that have broken down from larger plastic items and are now found in the water. Microplastics can harm aquatic organisms and potentially affect human health if they enter the food chain.
# 
# - Emerging contaminants: These are a wide range of chemicals, including pharmaceuticals, personal care products, and pesticides, that are increasingly being detected in water sources. These contaminants can have negative effects on human health and aquatic ecosystems, even at low levels.
# 
# - Microbial contamination: This refers to the presence of harmful bacteria, viruses, and parasites in the water, which can cause illness in humans and animals; admittedly a legacy pollutant, but still of importance - particularly novel and engineered pathogens.
# 
# These emergent measures are important because they reflect new and emerging threats to water quality, and can help us better understand the complex interactions between human activities and the environment. By monitoring and addressing these measures, we can better protect and preserve our water resources.
# 
# ## Modeling Dissolved Oxygen
# 
# Modeling dissolved oxygen in a river involves simulating the various physical, chemical, and biological processes that affect the concentration of dissolved oxygen in the water. Some of the key processes that need to be considered in a dissolved oxygen modeling framework are:
# 
# - Hydrodynamics: The flow of water in the river can affect the concentration of dissolved oxygen by transporting it downstream or mixing it with other water bodies.
# 
# - Oxygen demand: The rate at which dissolved oxygen is consumed by microorganisms, plant matter, and other organic materials in the river.
# 
# - Oxygen supply: The rate at which oxygen is supplied to the river through processes such as photosynthesis, atmospheric exchange, and inflows from upstream sources.
# 
# - Temperature: The temperature of the water affects the solubility of oxygen, with higher temperatures leading to lower levels of dissolved oxygen. Changes in water temperature can have significant impacts on aquatic ecosystems, including changes in the distribution and abundance of species, and the timing of important ecological processes such as migration and reproduction.
# 
# - Turbidity: The amount of suspended particles in the water can affect the penetration of sunlight, which in turn can impact photosynthesis and the production of dissolved oxygen.
# 
# - Nutrient levels: The presence of nutrients such as nitrogen and phosphorus can affect the growth of aquatic plants and algae, which in turn can affect the production of dissolved oxygen. Nutrient pollution can cause harmful algal blooms, which can be toxic to humans and wildlife, as well as deplete oxygen in the water, causing dead zones.
# 
# To model dissolved oxygen in a river, various mathematical models such as the Streeter-Phelps model, the one-dimensional water quality model, and the two-dimensional hydrodynamic water quality model can be used. These models incorporate the above processes and help predict the spatial and temporal variations in dissolved oxygen concentration in the river.
# 
# 
# 
# 
# 
# ## Some Common Models (Software)
# 
# There are several software programs available for modeling dissolved oxygen in rivers, some of which are:
# 
# - CE-QUAL-W2: This is a two-dimensional, laterally averaged, hydrodynamic and water quality model developed by the US Army Corps of Engineers. It simulates dissolved oxygen, temperature, nutrients, and algae dynamics in lakes, estuaries, and rivers.
# 
# - WASP: The Water Quality Analysis Simulation Program is a one-dimensional, dynamic, and steady-state model developed by the US Environmental Protection Agency. It models dissolved oxygen, temperature, nutrients, and organic matter dynamics in rivers and streams.
# 
# - EFDC: The Environmental Fluid Dynamics Code is a three-dimensional, hydrodynamic and water quality model developed by the US Army Corps of Engineers. It simulates dissolved oxygen, temperature, nutrients, algae, and sediment dynamics in estuaries, lakes, and rivers.
# 
# - QUAL2K: This is a one-dimensional, dynamic, and steady-state water quality model developed by the US Environmental Protection Agency. It simulates dissolved oxygen, temperature, nutrients, organic matter, and sediment dynamics in rivers and streams.
# 
# - MIKE 21/3: This is a suite of two-dimensional and three-dimensional hydrodynamic and water quality models developed by DHI Water & Environment. It simulates dissolved oxygen, temperature, nutrients, algae, and sediment dynamics in estuaries, lakes, and rivers.
# 
# These software programs provide different levels of complexity and features, and the choice of a particular program depends on the specific research questions, available data, and computational resources.
# 
# In this course we will use QUAL2E a predecesssor of QUAL2K above, its more-or-less the same computation engine - but using it server-side will save the need for installation.

# In[ ]:




