import os 
import streamlit as st 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.prompts import PromptTemplate

API_KEY = ""
os.environ['OPENAI_API_KEY'] = API_KEY
chat = ChatOpenAI(temperature=0.1, openai_api_key=API_KEY)


st.title('Climatebot ')
st.subheader('The scientific consensus asserts that climate change poses an immediate threat to humanity and urgent action is necessary. Climate deniers employ seven strategies to impede prompt action on addressing climate change.')
st.image("/Users/harikrishna/Downloads/pdfs/climateChart.png", width=300, use_column_width="auto")


UserPrompt = st.text_input('Input your argument here - the bot will classify it into one of the seven categories and give a rebuttal') 


explanation="""
1)	Outright Denial
Outright denial involves a total rejection of global warming and climate change, dismissing the vast amount of scientific data supporting it. Outright denial often involves rejecting data from climate studies, observations of increasing global temperatures, and the melting of ice caps and glaciers, presenting an alternate reality where climate change is either a hoax or a natural occurrence not linked to human activity. This form of discourse negates the foundational premise that there is a problem requiring urgent attention.

Examples:

Climate change is a natural cycle the Earth has gone through many times before; it's not caused by humans."

"There's no consensus among scientists about climate change; many believe it's just a hoax."

"The climate models are unreliable and have been wrong before, so we shouldn't trust their current predictions."

2)	Impact skepticism
Impact skepticism focuses on minimizing or disputing the predicted impacts of climate change on the environment, human life, and biodiversity. Skeptics of climate change impacts often acknowledge that the climate might be changing but argue that these changes are either beneficial, inconsequential, or manageable without significant intervention or alteration of current practices. This form of skepticism undermines the urgency regarding the need for immediate and disruptive action to mitigate climate change by suggesting that adaptation could be a viable strategy without acknowledging the proven dangers of climate change.
"The idea that climate change will lead to mass extinctions is exaggerated; most species will adjust or move."

"Species have always adapted to climate changes throughout history; a few degrees warmer won't make a difference."

"The benefits of global warming, like fewer winter deaths and increased crop yields in some regions, outweigh the negatives."

3)	Attacking the scientists and the scientific consensus
This category involves undermining the credibility of climate science and the scientific community that supports it. By attacking the integrity, motivations, and professionalism of scientists, and by suggesting that the scientific consensus on climate change is a result of bias, conspiracy, or flawed methodology, this approach seeks to sow doubt about the reliability of climate research. It diverts attention from the scientific findings and towards the characters of the scientists themselves, implying that climate change is a manufactured crisis. This tactic not only challenges the current understanding of climate change but also seeks to erase public trust in the scientific institutions and the  value it has as a basis for government policy.

"Climate scientists are only in it for the money and funding; they'll say anything to keep their grants."
"There's a global conspiracy among scientists to push the climate change agenda for political reasons."
"Many scientists who question climate change are silenced or ignored, so we're not getting the full picture."

4)	Push non transformative solutions

This category involves advocating for solutions that, while seemingly beneficial, do not significantly alter the status quo and fail to tackle the root causes of climate change. Proponents of non-transformative solutions place an overemphasis on technological advancements, market-based incentives, and incremental changes, often ignoring more impactful, systemic reforms. By promoting these less effective measures, attention is diverted away from the urgent need for comprehensive, transformative action.
"We just need to plant more trees; we don't need to stop using fossil fuels."
"Market forces and consumer choices will naturally lead us away from fossil fuels, so government intervention is unnecessary."
“Electric cars and solar panels are enough to tackle climate change; we don't need broader systemic changes."

5)	Emphasize the downsides
Discourses that emphasize the downsides focus on the potential negative impacts of climate action, such as economic costs, job losses, or lifestyle changes, often exaggerating these to overshadow the urgent need for action. This approach seeks to instill fear or resistance among the public and policymakers by presenting climate policies as harmful to societal well-being and economic stability. It neglects the long-term benefits of climate action and the far greater costs of inaction, creating a skewed perception that the repercussions of climate policies outweigh the climate crisis itself.
"Restricting carbon emissions will make energy too expensive for the poor."
"The cost of transitioning to renewable energy is too high for ordinary people."
"Implementing strict climate policies will kill jobs and hurt the economy."

6)	Redirect responsibility
This discourse aims to deflect accountability for addressing climate change, suggesting that the responsibility lies elsewhere. It includes shifting blame to individuals, other nations, or sectors, thereby diluting the sense of collective action needed to combat climate change. By arguing that others are more responsible or capable of making changes, this approach undermines the need for universal commitment and action. It conveniently ignores the interconnectedness of global emissions and the shared responsibility of all actors, from individuals to governments, in contributing to solutions.
“Our country has already done enough; other nations need to step up their efforts."

"Even if we cut all our emissions today, it wouldn't make a dent in global levels because of other countries' policies."

"Our contributions to global emissions are so small that any action we take won't significantly impact climate change."

7)	Surrender
The surrender discourse embodies a defeatist attitude towards climate action, suggesting that it is too late to make a difference or that the challenges are insurmountable. It fosters a sense of hopelessness and resignation, arguing that adaptation to the consequences of climate change is the only viable path. This narrative dismisses the potential of mitigation efforts and overlooks the significant progress that can still be made in avoiding the worst impacts of climate change. By promoting surrender, this discourse aims to extinguish the momentum for action and acceptance of the status quo.
"The scale of change needed is impossible to achieve; we might as well accept the inevitable."
"The challenges of global cooperation make effective action on climate change unachievable."
"Given the current political climate, meaningful action on climate change will never happen."

"""

if UserPrompt:
    strContent = str(chat([
        SystemMessage(content="You are ClimateBot, you are tasked with categorizing climate change arguments into one ofseven categories and giving a rebuttal"),
        HumanMessage(content="Classify it into one of the seven given categories: 1) Redirect responsibility 2) Pushing Non-Transformative Solutions 3) Emphasizing the Downsides 4) Surrendering to Climate Change 5)Denying climate change 6)Denying the effects of climate change 7)Attacking scientists and the scientific consenusus, and explain it:, if it falls into more than one category explain that as well"+explanation),
        AIMessage("I understand, I will classify the given climate change argument into one of the seven categories and give an explanation"),
        HumanMessage(content="Classify this argument: "+UserPrompt)
    ]))
    
    index1 = strContent.find("'")
    index2 = strContent.find('.')
    
    heading = "Category: " + strContent[index1-1:index2 + 1]  
    content = strContent[index2 + 1:].strip()
    
    st.write(heading)
    st.write(content)
