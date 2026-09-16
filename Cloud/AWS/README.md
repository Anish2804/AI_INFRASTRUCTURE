# Virtualization & Virtual Machines (VMs)

## 1. Virtualization kya hai?

**Virtualization** ek technology hai jisme ek hi physical computer ke hardware resources:

* RAM
* CPU
* Storage

ka use karke **multiple Operating Systems** run kiye ja sakte hain.

---

## 2. Hypervisor ki Role

**Hypervisor** ek software hai jo virtualization ko possible banata hai.

Ye main/physical machine ke resources ko different parts mein divide karke **Virtual Machines (VMs)** create karta hai.

**Example:** Oracle VirtualBox

---

## 3. Virtual Machine (VM) kaise kaam karti hai?

Har VM ek **mini computer** ki tarah kaam karti hai.

VM **isolated** hoti hai.

Matlab:

> Ek VM mein hone wali problem normally main (host) machine ko affect nahi karti.

---

## 4. Types of Hypervisor

### Type 2 — Hosted Hypervisor

* Main Operating System (jaise Windows) ke upar install hota hai.
* Example: Oracle VirtualBox

```text
Hardware
   ↓
Host OS
   ↓
Type 2 Hypervisor
   ↓
VM
```

### Type 1 — Bare Metal Hypervisor

* Directly hardware par install hota hai.
* Iske liye alag Host OS ki zarurat nahi hoti.
* Servers mein use hota hai.
* Examples:

  * VMware vSphere
  * Citrix XenServer

```text
Hardware
   ↓
Type 1 Hypervisor
   ↓
VM
```

### Type 1 vs Type 2

| Type 1                    | Type 2                                     |
| ------------------------- | ------------------------------------------ |
| Directly hardware par     | Host OS ke upar                            |
| Host OS ki zarurat nahi   | Host OS required                           |
| Servers mein use hota hai | Desktop environments mein use ho sakta hai |

---

## 5. Virtualization ke Benefits

### 1. Cost & Space Saving

Multiple machines ko ek hi physical hardware par run kiya ja sakta hai.

### 2. Scalability

Requirement ke according resources ko **increase ya decrease** karna easy hota hai.

### 3. Maintenance

Cloud providers jaise **AWS** security aur updates ka responsibility lete hain, jisse company ka maintenance work easy ho jata hai.

---

# Quick Revision

* **Virtualization** → Ek physical computer par multiple OS run karna.
* **Hypervisor** → VMs create karta hai aur hardware resources manage/divide karta hai.
* **VM** → Ek isolated mini computer.
* **Type 2** → Host OS ke upar run hota hai.
* **Type 1** → Directly hardware par run hota hai.
* **Type 1** → Servers mein use hota hai.
* Virtualization ke benefits → **Cost/Space Saving + Scalability + Easier Maintenance**.






# Cloud Computing

## 1. Cloud Computing kya hai?

**Cloud Computing** ka matlab hai internet ke through IT resources ko **on-demand** use karna aur **Pay-as-you-go** basis par payment karna.

IT resources mein include ho sakte hain:

* Servers
* Storage
* Databases
* Software

### Examples

* Google Drive
* iCloud

### Major Cloud Providers

* AWS (Amazon Web Services)
* Microsoft Azure
* Google Cloud

---

## 2. Cloud kaise kaam karta hai?

Cloud providers ke paas large **Data Centers** hote hain.

Ye **Virtualization** ka use karke ek hi physical hardware ko multiple customers ke beech share karte hain.

```text
Large Data Center
       ↓
Physical Hardware
       ↓
Virtualization
       ↓
Multiple Customers
```

---

## 3. Cloud ki zarurat kyun hai?

Agar company apna business, jaise e-commerce, start karti hai toh khud:

* Servers purchase karne
* Security manage karne
* Backups manage karne

pad sakte hain.

Cloud provider ye infrastructure responsibilities handle karta hai, aur company resources ko rent/subscription basis par use kar sakti hai.

### Benefits

* **Scalability** → Resources ko requirement ke according increase/decrease karna easy.
* **Flexibility** → Infrastructure ko easily adjust kar sakte hain.

---

# 4. Cloud Computing Service Models

Cloud services ke 3 main models:

## IaaS — Infrastructure as a Service

Isme basic **infrastructure/hardware** rent par milta hai.

OS aur applications ko khud manage karna hota hai.

```text
IaaS
↓
Infrastructure
↓
You manage OS + Application
```

**Example analogy:** Khali shop — infrastructure available hai, baaki setup khud karna hai.

---

## PaaS — Platform as a Service

Isme **ready platform** milta hai.

Aap mainly apni **application** par focus karte ho; hardware aur OS ki concern nahi hoti.

```text
PaaS
↓
Ready Platform
↓
You focus on Application
```

**Example analogy:** Furniture aur machines wali ready shop.

---

## SaaS — Software as a Service

Isme **fully ready software** milta hai.

Kuch install/manage karne ki zarurat nahi; internet ke through directly access karte ho.

```text
SaaS
↓
Ready Software
↓
Just Use It
```

**Example analogy:** Ice-cream vending machine.

---

## IaaS vs PaaS vs SaaS

| IaaS                    | PaaS                  | SaaS             |
| ----------------------- | --------------------- | ---------------- |
| Infrastructure          | Ready Platform        | Ready Software   |
| OS khud manage          | OS ki concern nahi    | Kuch manage nahi |
| Application khud manage | Application par focus | Directly use     |

---

# 5. Cloud Deployment Models

## Public Cloud

* Shared environment
* Relatively cheaper aur easy
* Privacy comparatively kam

**Analogy:** Public Transport

---

## Private Cloud

* Sirf ek organization ke liye dedicated
* More control
* More security

**Analogy:** Rental Car

---

## Hybrid Cloud

**Public + Private Cloud** ka combination.

Sensitive data ko **Private Cloud** mein aur baaki resources ko **Public Cloud** mein rakha ja sakta hai.

```text
Hybrid Cloud
     │
 ┌───┴────┐
 ↓        ↓
Private  Public
Sensitive  Other
Data       Resources
```

---

# 6. Cloud mein sirf Servers nahi hote

Cloud providers multiple types ki services provide karte hain, jaise:

* Servers
* Databases
* Storage
* Machine Learning
* Monitoring
* Networking

---

# Quick Revision

* **Cloud Computing** → Internet ke through IT resources ko on-demand use karna + Pay-as-you-go.
* Cloud providers → **AWS, Azure, Google Cloud**
* Cloud providers large **Data Centers** use karte hain.
* **Virtualization** → Same hardware ko multiple customers ke beech share karne mein help karti hai.
* **IaaS** → Infrastructure milta hai.
* **PaaS** → Ready platform milta hai.
* **SaaS** → Ready software milta hai.
* **Public Cloud** → Shared environment.
* **Private Cloud** → Dedicated to one organization.
* **Hybrid Cloud** → Public + Private.
* Cloud services → Servers, Storage, Database, ML, Monitoring, Networking etc.





# Amazon Web Services (AWS) — Overview

## 1. AWS kya hai?

**AWS (Amazon Web Services)** ek **Cloud Computing Service Provider** hai.

Ye cloud ke through different IT services aur infrastructure provide karta hai.

---

## 2. AWS History & Growth

* **2006** mein AWS launch hua.
* Initially mainly:

  * **S3** → Storage
  * **EC2** → Compute
* Aaj AWS mein **200+ fully-featured services** available hain, including AI, ML, IoT etc.

---

## 3. AWS Popular kyun hai?

AWS ke 4 main pillars:

### Scalability

Requirement ke according resources ko **increase ya decrease** kar sakte hain.

### Global Reach

AWS ke servers/infrastructure duniya ke different regions mein available hain.

### Reliability

AWS ek mature aur widely used cloud platform hai.

### Security

AWS high-level security standards provide karta hai.

---

## 4. AWS Market Share

**2024 report** ke according AWS ka approximately **32% cloud market share** tha.

---

## 5. Popular AWS Services

| Service        | Use                  |
| -------------- | -------------------- |
| **EC2**        | Computing            |
| **S3**         | Storage              |
| **RDS**        | Database             |
| **Lambda**     | Serverless Computing |
| **CloudFront** | Content Delivery     |

---

## 6. AWS Infrastructure

### Region

AWS ka infrastructure different **Regions** mein distributed hota hai.

### Availability Zone (AZ)

Ek Region ke andar multiple **Availability Zones** hote hain.

AZs ka purpose ye hai ki agar ek data center/AZ mein failure ho, toh doosra available reh sake.

```text
Region
│
├── Availability Zone 1
│
├── Availability Zone 2
│
└── Availability Zone 3
```

Isse **Single Point of Failure** se bachne mein help milti hai.

### AWS Infrastructure Numbers

Video ke according:

* **34 Regions**
* **108 Availability Zones**

### Local Zones

**Local Zones** ultra-low latency ke liye use hote hain.

---

## 7. AWS Pricing

### Pricing Calculator

AWS ka **Pricing Calculator** use karke services ka cost pehle se estimate kiya ja sakta hai.

### Free Tier

Beginners/students ke liye AWS limited resources free provide karta hai.

Video mein example:

* **750 hours EC2**

> Free Tier ke exact limits/time-period ko use karne se pehle current AWS terms check karna chahiye.

---

## 8. Career Opportunities

AWS seekhne ke baad different roles mein ja sakte hain, jaise:

* Cloud Architect
* DevOps Engineer
* Data Engineer
* Solutions Architect

---

# Quick Revision

* **AWS** → Cloud Computing Service Provider.
* AWS launched → **2006**
* Initial services → **S3 + EC2**
* AWS → **200+ services**
* 4 pillars → **Scalability + Global Reach + Reliability + Security**
* **EC2** → Compute
* **S3** → Storage
* **RDS** → Database
* **Lambda** → Serverless
* **CloudFront** → Content Delivery
* **Region** → AWS infrastructure ka geographical area.
* **AZ** → Region ke andar isolated infrastructure location.
* Multiple AZs → Failure/Single Point of Failure se protection.
* **Local Zones** → Ultra-low latency.
* **Pricing Calculator** → Cost estimate.
* AWS career roles → Cloud Architect, DevOps Engineer, Data Engineer, Solutions Architect.




