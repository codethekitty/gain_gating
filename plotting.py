from pylab import *
import pandas
df = pandas.read_csv('gain_gating.csv',index_col=0)
#%%
figure(figsize=(12,8))
subplot(211)
plot(df.sort_values(by='Gain').Gain,'-',lw=4,label='Actual')
plot(df.sort_values(by='Gain').Gain_A,'d-',label='Adam')
plot(df.sort_values(by='Gain').Gain_C,'s-',label='Calvin')
xticks(rotation=45,ha='right')
ylabel('# GAIN')
legend()

subplot(212)
plot(df.sort_values(by='Gating').Gating,'-',lw=4,label='Actual')
plot(df.sort_values(by='Gating').Gate_A,'d-',label='Adam')
plot(df.sort_values(by='Gating').Gate_C,'s-',label='Calvin')
xticks(rotation=45,ha='right')
ylabel('# GATING')
tight_layout()

savefig('temp.png',dpi=150,bbox_inches='tight')
