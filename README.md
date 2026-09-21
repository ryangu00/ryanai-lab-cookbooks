![banner](docs/assets/banner.png)

# RyanAI Lab cookbooks — index

Part of RyanAI Lab. One repository per experiment; each one carries its own numbers, pitfalls and reproduction steps. This page only tells you which one to open.

## Start here

**"I run one or two Dell Pro Max with GB10 nodes and want to serve a model"**

1. [dell-pro-max-gb10-uma-memory-pitfalls](https://github.com/ryangu00/dell-pro-max-gb10-uma-memory-pitfalls) — the unified-memory incidents every node operator hits first.
2. [dell-pro-max-gb10-qsfp-dual-rail](https://github.com/ryangu00/dell-pro-max-gb10-qsfp-dual-rail) — cabling and NCCL rail naming that decides two-node throughput.
3. [dell-pro-max-gb10-qwen3.8-flash-next](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next) and [dell-pro-max-gb10-deepseek-v4-flash-vision-exp](https://github.com/ryangu00/dell-pro-max-gb10-deepseek-v4-flash-vision-exp) — the two two-node serving books (TP2, long context, vision).
4. [dell-pro-max-gb10-qwen3.8-27b](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-27b) and [dell-pro-max-gb10-gpt-oss-120b](https://github.com/ryangu00/dell-pro-max-gb10-gpt-oss-120b) — the single-node books, one engine-native, one release-software.

**"I want to fine-tune on this hardware"**

1. [training-weights-vs-context](https://github.com/ryangu00/training-weights-vs-context) — when fine-tuning helps and when it does not; read this before training anything.
2. [training-sft-ablation-discipline](https://github.com/ryangu00/training-sft-ablation-discipline) — how to ablate a regression instead of re-tuning blindly.
3. [training-moe-lora-cpt-gb10](https://github.com/ryangu00/training-moe-lora-cpt-gb10) — full continued pre-training plus LoRA/SFT of a MoE on one node.
4. [training-vl-lora-qwen3.8-27b](https://github.com/ryangu00/training-vl-lora-qwen3.8-27b) — a vision LoRA trained and hot-plugged into a running server.

**"I want to know whether a model is good for MY work"**

1. [ryanai-evalbank](https://github.com/ryangu00/ryanai-evalbank) — the method for scoring a model on your own work without publishing the questions.
2. [dell-pro-max-gb10-qwen3.8-flash-next-agentic-thinking](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next-agentic-thinking) — why the measurement setting, not the model, decided an agentic gap.
3. [dell-pro-max-gb10-qwen3.8-flash-next-engine-ab](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next-engine-ab) — the engine-form A/B the setting change made possible.

## Two-node serving on Dell Pro Max with GB10

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [dell-pro-max-gb10-qwen3.8-flash-next](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next) | Dual-node deployment of a new-architecture GDN+QSA model, from a 50K safety line to a 1M-context production engine. | You are standing up this model on two nodes. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.8-flash-next-1m-context](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next-1m-context) | Extending the model from native 262K context to a 1M window with static YaRN rope scaling, measured. | You need a validated long-context recipe, not guesses. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.8-flash-next-agentic-thinking](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next-agentic-thinking) | A failed agentic gate shown to be a measurement setting, fixed by enabling thinking mode. | Your model "fails" agentic evaluation and you suspect the harness. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.8-flash-next-engine-ab](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-flash-next-engine-ab) | A one-night A/B of engine forms: native 262K vs YaRN variants vs KV precision vs MTP off. | You are choosing between engine configurations of the same weights. | current | 2026-09-20 |
| [dell-pro-max-gb10-vllm-mtp-async-runaway](https://github.com/ryangu00/dell-pro-max-gb10-vllm-mtp-async-runaway) | Runaway repetition loops from async scheduling combined with MTP, and the one-flag fix. | Your stack repeats itself under real agentic load. | current | 2026-09-20 |
| [dell-pro-max-gb10-vllm-stack-ab](https://github.com/ryangu00/dell-pro-max-gb10-vllm-stack-ab) | A/B of vLLM serving stacks for two-node deployment. | You are picking a serving stack rather than a model. | current | 2026-09-17 |
| [dell-pro-max-gb10-zero-downtime-model-swap](https://github.com/ryangu00/dell-pro-max-gb10-zero-downtime-model-swap) | Swapping the engine from one model stack to another with zero changes on consumer surfaces. | You must change engines without breaking callers. | current | 2026-09-20 |
| [dell-pro-max-gb10-deepseek-v4-flash-vision-exp](https://github.com/ryangu00/dell-pro-max-gb10-deepseek-v4-flash-vision-exp) | Two-node tensor-parallel serving of vision-enhanced weights with long context and image input. | You want a two-node production stack with vision. | current | 2026-09-20 |
| [dell-pro-max-gb10-dual-node-model-bakeoff-2026-05](https://github.com/ryangu00/dell-pro-max-gb10-dual-node-model-bakeoff-2026-05) | Head-to-head selection benchmark across four candidate models on a private question suite. | You are comparing candidate models for a two-node purchase or deployment. | historical | 2026-09-20 |

## Single-node serving on Dell Pro Max with GB10

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [dell-pro-max-gb10-qwen3.8-27b](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-27b) | Single-machine deployment of Qwen3.8-27B with quantization, speculative decoding and a hot-plugged vision tower. | You want the single-node workhorse setup. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.8-27b-mtp-k-sweep](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-27b-mtp-k-sweep) | Four rounds of community-proposed serving tuning, all rolled back, with the evidence. | A tuning recipe from the internet looks tempting. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.8-27b-dflash2-exl3](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.8-27b-dflash2-exl3) | Head-to-head of an EXL3 quantized serving stack against the production vLLM stack for the same model. | You are considering exllamav3 instead of vLLM. | current | 2026-09-20 |
| [dell-pro-max-gb10-qwen3.6-35b-a3b-nvfp4-mtp](https://github.com/ryangu00/dell-pro-max-gb10-qwen3.6-35b-a3b-nvfp4-mtp) | NVFP4 serving of Qwen3.6-35B-A3B with speculative decoding and alternative MoE/attention backends. | You want to know if this model works on one node. | historical | 2026-09-20 |
| [dell-pro-max-gb10-muse-glimmer-30b](https://github.com/ryangu00/dell-pro-max-gb10-muse-glimmer-30b) | Deployment of the open-weight Muse family member, ending in a negative result against the incumbent. | You are evaluating this model family. | current | 2026-09-20 |
| [dell-pro-max-gb10-glm-5.3-flash](https://github.com/ryangu00/dell-pro-max-gb10-glm-5.3-flash) | Full record of a no-go verdict for a dual-machine deployment after a full day of testing. | You want the failure case before trying it yourself. | current | 2026-09-03 |
| [dell-pro-max-gb10-gpt-oss-120b](https://github.com/ryangu00/dell-pro-max-gb10-gpt-oss-120b) | A frontier-class 120B on one node at stable throughput on release software, zero patches. | You want a big model on one box without patching. | current | 2026-09-03 |
| [dell-pro-max-gb10-qwen-int4-122b](https://github.com/ryangu00/dell-pro-max-gb10-qwen-int4-122b) | Our earliest resident production config and the incident-driven ops hardening around it. | You are building ops discipline around a resident service. | current | 2026-09-03 |
| [dell-pro-max-gb10-deepseek-v4-flash-exl3](https://github.com/ryangu00/dell-pro-max-gb10-deepseek-v4-flash-exl3) | EXL3 quantization, one machine, one seat, ultra-long context. | You want a single-seat long-context workstation, not concurrency. | current | 2026-09-03 |
| [dell-pro-max-gb10-thinking-tier-proxy](https://github.com/ryangu00/dell-pro-max-gb10-thinking-tier-proxy) | A thin proxy where the local port decides whether and how hard a request thinks. | You want thinking tiers without touching the engine. | current | 2026-09-20 |
| [dell-pro-max-gb10-ollama-toolbox](https://github.com/ryangu00/dell-pro-max-gb10-ollama-toolbox) | The utility-slot models around a main workhorse: vision fallback, page extraction, embedding. | You are filling the small model slots next to your LLM. | current | 2026-09-03 |
| [dell-pro-max-gb10-kvbm-ssd-kv-cache](https://github.com/ryangu00/dell-pro-max-gb10-kvbm-ssd-kv-cache) | A minimal measured test of three-tier KV-cache offload, kept for the evidence, not a recommendation. | You are tempted by KV-cache offload to disk. | current | 2026-09-18 |

## Hardware and OS

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [dell-pro-max-gb10-uma-memory-pitfalls](https://github.com/ryangu00/dell-pro-max-gb10-uma-memory-pitfalls) | Seven incidents where unified memory (CPU and GPU sharing it) caused OOM or worse, with the healing patterns. | Anything on this hardware OOMs and you do not know why. | current | 2026-09-20 |
| [dell-pro-max-gb10-ota-kernel7-kho](https://github.com/ryangu00/dell-pro-max-gb10-ota-kernel7-kho) | Upgrading both nodes across a major kernel, driver and grub change without bricking. | An OTA is overdue and you are afraid of it. | current | 2026-09-20 |
| [dell-pro-max-gb10-qsfp-dual-rail](https://github.com/ryangu00/dell-pro-max-gb10-qsfp-dual-rail) | A community finding about the QSFP port enumerating as two virtual NICs, verified on hardware back-to-back. | Your two-node bandwidth is half of what it should be. | current | 2026-09-20 |

## Training on Dell Pro Max with GB10

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [training-moe-lora-cpt-gb10](https://github.com/ryangu00/training-moe-lora-cpt-gb10) | A measured walkthrough of continued pre-training plus LoRA/SFT of a 35B-A3B MoE on one node. | You are attempting full pre-training-scale work on one box. | current | 2026-09-20 |
| [training-sft-ablation-discipline](https://github.com/ryangu00/training-sft-ablation-discipline) | A factorial ablation that traced a regression to its cause and measured the base inside the drift band. | Two things changed at once and quality dropped. | current | 2026-09-20 |
| [training-weights-vs-context](https://github.com/ryangu00/training-weights-vs-context) | Three capability specialisations of one base family, each attempted by weights first, each gated by the same guardrail. | You cannot decide between fine-tuning and context. | current | 2026-09-20 |
| [training-vl-lora-qwen3.8-27b](https://github.com/ryangu00/training-vl-lora-qwen3.8-27b) | Training a vision LoRA on a public chart dataset and hot-plugging it into a running server. | You want a trained adapter live without a restart. | current | 2026-09-20 |
| [training-embedding-finetune](https://github.com/ryangu00/training-embedding-finetune) | Fine-tuning an embedding model on your own corpus style and deploying it as a resident service. | Your retrieval misses and your domain vocabulary is odd. | current | 2026-09-20 |
| [training-reranker](https://github.com/ryangu00/training-reranker) | Self-hosting and training a reranker, plus a community-scale pitfall where a bad file masqueraded as a weak model. | Your precision ranking stage needs work. | current | 2026-09-03 |

## Apple silicon

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [apple-silicon-qwen3-235b-a22b](https://github.com/ryangu00/apple-silicon-qwen3-235b-a22b) | A real-world record of running a 235B MoE on a large-unified-memory Mac, ending in a deliberate retirement. | You wonder whether a huge MoE fits on a Mac. | current | 2026-09-03 |
| [apple-silicon-qwen3.6-27b](https://github.com/ryangu00/apple-silicon-qwen3.6-27b) | The sweet-spot selection story for a local model on a 64GB Mac. | You are choosing the default local model for a 64GB Mac. | current | 2026-09-03 |
| [apple-silicon-wemm-embedding](https://github.com/ryangu00/apple-silicon-wemm-embedding) | Replacing the image-embedding model behind a personal knowledge base, measured end to end. | Your image search needs a better embedding model. | current | 2026-09-10 |

## Retrieval, embeddings and agents

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [agentic-rag-from-scratch](https://github.com/ryangu00/agentic-rag-from-scratch) | Building agentic retrieval-augmented generation from first principles. | You are building an agentic RAG loop yourself. | current | 2026-09-03 |
| [pgvector-bilingual-embedding-selection](https://github.com/ryangu00/pgvector-bilingual-embedding-selection) | A measured selection of a bilingual text-embedding model, including the HNSW limit and a config hazard. | Your knowledge base is bilingual and your embeddings underperform. | current | 2026-09-20 |
| [westpoint-agent-eval-rigged-sandbox](https://github.com/ryangu00/westpoint-agent-eval-rigged-sandbox) | WestPoint: an agent evaluation inside a deliberately rigged sandbox. | You are evaluating agents in an environment built to be adversarial. | current | 2026-09-03 |
| [deepseek-harness-three-knobs](https://github.com/ryangu00/deepseek-harness-three-knobs) | A measured test of three community-proposed levers on DeepSeek Harness, all opt-in, against a measured baseline. | Someone proposed a harness tweak and you want the verdict first. | current | 2026-09-20 |

## Evaluation method

| repo | what it is | read it when | status | updated |
|---|---|---|---|---|
| [ryanai-evalbank](https://github.com/ryangu00/ryanai-evalbank) | A method and harness for scoring a model on your own work, without publishing the questions. | You want numbers that describe your workload, not someone else's. | current | 2026-09-20 |

## How these were made

Every number in these books is first-hand, measured on the named hardware. The questions of our private evaluation bank are never published; only the method is. Every repository went through an independent two-lens review — privacy line by line, rigor number by number — before publication. The author identity is in each LICENSE.

## Conventions

- "Two nodes" always means two Dell Pro Max with GB10 nodes (head node + worker node, TP2 over RoCE).
- Scores are medians of two runs, with the spread reported.
- A category where the incumbent scores ≥ 95 is a ceiling, not a result.
- Nothing here is a benchmark ranking for the reader; it is a record of our own measurements.

## License

Apache-2.0, as in [LICENSE](LICENSE).
