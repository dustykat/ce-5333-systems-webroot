#!/usr/bin/env python
# coding: utf-8

# # Introduction

# ## Water Resources Management Concepts
# 
# Three Water Resources (Engineering-Type) related activities are: Water Resources Development (WRD), Water Resources Planning (WRP), and Water Resources Management (WRM). 
# 
# **Water Resources Development** is defined as: actions, both physical and administrative that lead to the beneficial use of water resources for single or multiple purposes.
# 
# :::{note}
# People from different backgrounds seldom have the same idea about what water resources development means. 
# To those living in an arid country, it means drought relief, food, jobs, law and politics. 
# To those living in humid areas, it brings to mind waterworks, flood protection, navigation, hydropower and pollution control. 
# To the ecologist, water resources development is often connected with the deterioration of habitats, the destruction of natural rivers and pollution. 
# To the water resources engineer, water resources development is related to dams, reservoirs, flood protection, diversions, river training, water treatment and reclamation. 
# To the lawyer, a water resource system is a device for the implementation of water rights. To the economist, water resources development is connected with economic efficiency, stimulation of growth, poverty alleviation and employment generation. Similar specialized viewpoints are held by politicians and decision makers.
# 
# Water resources development most certainly includes all these points of view. It is physical, economic, political, sociological, environmental, agricultural and technical. The relative ease with which one of these aspects might be quantifiable, as compared to another, does not in any way reflect a correspondingly great importance. If not enough weight is given to either one of these aspects, a water resources development project is likely to fail.
# :::
# 
# **Water Resources Planning** is defined as: planning of the development and *allocation* of a *scarce* resource (sectoral and intersectoral), matching water availability and demand, taking into account the full set of national objectives and constraints and the interests of stakeholders
# 
# **Water Resources Management** is defined as: the set of technical, institutional, managerial,legal and operational acitivities required to plan, develop, operate and manage water resources.
# 
# Water Resources Management can be considered as a process including all activities of planning, design, construction and operation of water resources systems.
# Hence: WRM is a superset containing WRP and to a large extent WRD.
# 
# Water Resources Management integrates by definition all aspects and functions related to water. The term integrated Water Resources Management. IWRM. is defined as WRM that takes full account of:
# - all natural aspects of the water resources system: surface water, groundwater, water quality (physical, biological and chemical) and its physical behaviour;
# - the interests of water users in all sectors of the national economy (agriculture, water supply, hydropower, inland transportation, fisheries, recreation, environment, nature conservation); hence the complete mix of inputs and outputs related to water;
# - the relevant national objectives and constraints (social, legal, institutional, financial, environmental);
# - the institutional framework and stakeholders (national, provincial, local); 
# - the spatial variation of resources and demands (upstream-downstream interaction, basin-wide analysis, interbasin transfer).
# 
# Good water resources management is integrated water resources management and the addition of the word 'integrated' is merely used for marketing.

# ## Sustainable Use of Water Resources
# 
# Water resources development that is not sustainable is ill-planned. 
# Fresh water resources are scarce and to a large extent finite. Although surface water may be considered a renewable resource, it only constitutes 1.5% of all terrestrial fresh water resources; the vast majority is groundwater (98.5%) which - at a human lifetime scale - is virtually unrenewable. 
# Consequently, there are numerous ways to jeopardize the future use of water, either by overexploitation (mining) of resources or by destroying resources for future use (e.g. pollution). 
# Besides physical aspects of sustainability there are social, financial and institutional aspects. 
# Some aspects of sustainability to consider are:
# - technical sustainability (balanced demand and supply, no mining) 
# - financial sustainability (cost recovery)
# - social sustainability (stability of population, stability of demand, willingness to "pay")
# - economic sustainability (sustaining economic development or welfare and production)
# - institutional sustainability (capacity to plan, manage and operate the system)
# - environmental sustainability (no long-term negative or irreversible effects)

# 

# ## Water Resources Management Activities
# 
# The management of the development of water resources is a complex activity. 
# It comprises the full range of activities in the development of water resources, from demand analysis through planning, design and construction to operation and monitoring. 
# In a sense, these activities are sequential: analysis comes before planning, and planning comes before design; but more importantly, there are numerous places in the process where loopbacks and feedbacks occur, where new information informs new views and new decisions have to be taken. 
# Water Resources Management (WRM) is a substantially dynamic process, covering a wide spectrum of activities in the fields of assessment, planning and operation. Some of these are:
# 
# **Assessment:**
# 
#  - water resources assessment
#  - environmental assessment 
#  
# **Planning:**
# 
#  - problem analysis
#  - activity analysis
#  - demand analysis
#  - formulation of objectives and constraints 
#  - demand forecasting
#  - design of alternative water resource systems
#  - system analysis
#  - system simulation and optimization
#  - sensitivity analysis
#  - multicriteria and multiconstraints trade-off analysis selection and decision making
#  - involvement of stakeholders
#  - communication, negotiation and conflict resolution
#  
# **Operation:**
# 
#  - allocation of resources
#  - demand management
#  - management and administration of water institutions operation and maintenance
#  - monitoring and evaluation
#  - financial management and performance auditing
#  
# The activities are multidisciplinary, involving, engineers in the area of hydrology, hydraulics, construction, water supply, sanitation, hydropower, irrigation, and non- engineers such as: environmentalists, ecologists, lawyers, economists, sociologists, agriculturists, politicians and representatives of interested parties, pressure groups, and water users.
# 
# In this list, the activities are not yet structured, they are a mere enumeration of activities involved in planning and management. 
# Later on in this treatise the relations between the planning activities and the steps to be followed in a planning cycle are presented.
# In our definition, WRM includes WRP. 
# 
# The expression that water resources planning and management is largely identical to water resources management is incomplete. 
# However, there is good reason to consider WRP as a separate activity within WRM. 
# Many of the complexities of WRM are related to the planning of the development of the resources. 
# Techniques to cope with uncertainty, to compare alternatives for development and select the most promising alternative, which may be considered the major challenges of WRM, lie in the field of planning. 
# WRP is a **permanent** activity, not only on a national or regional scale, but at the scale of any complex water resources system. Such a system is never completed in the sense that no further development is possible or necessary. 
# The planned system is implemented in stages, each stage lasting sometimes several years, and the changing technology, demand, political and socio-economical conditions require a permanent readjustment of the existing system and an adjustment of the planned development. 
# The planning of water resources development, thus, has a sufficiently large domain for engineers to exclusively specialize in. 
# However, as a result of the many moments of decision making which occur during the planning process, there is a close interaction with management. 
# Consequently the activity is and should be fully integrated in WRM.
# 
# In the past, there was a strong bias in WRP to optimization; so strong, that to some people, WRP was almost identical to optimization (linear programming, dynamic programming, etc). Nowadays, it is widely recognised that optimization techniques serve a valuable supportive purpose, but are only part of an overall toolkit. 
# The reason for this psuedo-abandonment of optimization lies in a few key elements of planning, which are largely responsible for the complexity of WRP:
# 
# - uncertainty of scenarios
# - conflict of interests
# - political reality.
# 
# :::{note}
# And optimization is hard. It never guarentees useful solutions, its computationally complex, and fairly difficult to explain with pictures and arrows and paragraphs on the back explaining each one.  Its also valuable and used with some ingenuity, can guide one to either good decisions or identify missing information.
# :::
# 
# If there were no uncertainty and conflict of interest, the planning of water resources would indeed be a simple optimization problem. In addition, the political reality of the moment does not always permit the implementation of "optimal" solutions. The final decision is generally a result of the balance of power. Optimization is only useful as a component of WRP where boundary conditions can be considered as fixed.

# ## Coping With Uncertainty
# 
# Uncertainty exists in almost all scenarios that form the boundary conditions for planning:
# - hydrologic scenarios: occurrence of droughts, floods disasters; within the full spectrum of uncertainty probably the most simple scenario to forecast with a reasonable accuracy;
# - financial and economic scenarios: the development of commodity prices, energy prices, exchange rates, or inflation;
# - socio-economic scenarios: population growth, level of consumption, unemployment rates, willingness to pay, mentality, acceptability of measures, attention of the public for water issues;
# - political scenarios: changes in government, changes in political system, outbreak of wars, policy changes, e.g. towards small scale versus large scale, the question of whether the emphasis will lie on guaranteeing some of the water for all, or most of the water for some, privatized or subsidized water, development of bilateral relations between riparian countries which share a river basin;
# - technological scenarios: the capacity to develop resources for a certain price will change as a function of the technology available.
# 
# Some of these scenarios are highly unpredictable and depend on global developments such as energy prices, international conflicts, economic recession, etc. A plan which has been shown to be "optimal" in relation to a certain combination of the above scenarios may prove the "worst" scenario under another combination of scenarios.
# 
# This could easily lead to the cynical conclusion that the only thing sure about a plan is that it will not come true. However, there are ways to cope with uncertainty; and some of the techniques involved are briefly discussed below.
# 
# The objective of planning should not be to just find the "optimal" alternative; it should search for an alternative which behaves well under a wide range of different scenarios. Such a plan is called a "robust" plan ("non-inferior", or "good enough"). 
# If alternative plans are evaluated for their robustness instead of their optimal performance, a much better basis is created for future development. A robust plan keeps as many options as possible open for future development. 
# This approach of taking a short term decision that leaves maximum scope for future policy changes is also called strategic planning.
# An important technique to check alternatives for robustness is sensitivity analysis. If the performance of a certain alternative is very sensitive to a boundary condition incorporating a high level of uncertainty, then the alternative ranks low.
# 
# Because water resources planning is a permanent activity, the objectives, constraints and boundary conditions of a planning process may, and probably will, change during the
# nas t0
# planning period. As a result of this uncertainty the planning has to be flexible,
# It has to allow loopbacks, feedbacks, and adjustments to be made to incorporate new information, new interests or new policies. 
# Also the appearance of new techniques, software and hardware, or new insights may lead planners to reconsider certain options.
# 
# The tools used to show the effect of different policies, scenarios, and alternative measures on the output of a complicated water resource system should also be flexible. They should not be so complicated that they take a long time to get started or to make adjustments. 
# If calibration or adjustments take too long, then the opportunity for strategic decision making may be lost. 
# They should be highly interactive and flexible simulation tools that can readily be adjusted to new views or new information to give relevant outputs to the water manager.

# ## Exercises

# ## References
