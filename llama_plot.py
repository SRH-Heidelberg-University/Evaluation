import matplotlib.pyplot as plt
import pandas

df = pandas.read_excel('llama.xlsx')

plt.figure(figsize=(10, 6))

df['context_precision'] = df['context_precision'] * 100
df['faithfulness'] =df['faithfulness'] * 100
df['answer_correctness'] = df['answer_correctness'] * 100
df['context_recall'] = df['context_recall'] * 100

print('Average Answer Correctness:',df['answer_correctness'].mean())
print('Average Context Precision:',df['context_precision'].mean())
print('Average Context Recall',df['context_recall'].mean())
print('Average Faithfulness:',df['faithfulness'].mean())

plt.plot(df['questions'], df['context_precision'], marker='o', label='Context Precision')
plt.plot(df['questions'], df['faithfulness'], marker='o', label='Faithfulness')
plt.plot(df['questions'], df['answer_correctness'], marker='o', label='Answer Correctness')
plt.plot(df['questions'], df['context_recall'], marker='o', label='Context Recall')

plt.title('RAGAS Evaluation Metrics for LLAMA')
plt.xlabel('QUESTIONS')
plt.ylabel('SCORE')
plt.xticks(df['questions'])
plt.legend()
plt.grid(False)
plt.tight_layout()

plt.show()
