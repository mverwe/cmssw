#ifndef Cond_PayloadWrapper_h
#define Cond_PayloadWrapper_h


#include "POOLCore/Ptr.h"

namespace cond {

  /** base class of IOV payload wapper
      the final class will include ptrs for payload and its summary
   */
  class  PayloadWrapper {
  public:
    ~PayloadWrapper(){}
    

    // load DOES NOT throw!
    virtual void loadAll() const {
      loadData();
      loadSummary();
    }

    bool loadData() const =0;
    bool loadSummary() const =0;



  };


  /** base class of IOV payload wrapper (no summary)
   */
  template<typename O> 
  DataWrapper : public PayloadWrapper {
  public:
    typedef PayloadWrapper base;
    typedef O Object; 
    typedef Object value_type; 
    typedef PayloadWrapper<value_type> self;
 
    
    explicit DataWrapper(Object * obj) : m_data(obj){}

    ~DataWrapper() {
      if (m_data.isLoaded()) delete m_data.get();
    }    

    
    Object const & data() const { return *m_data;}

    bool loadData() const {
      return m_data.get();
    }

  private:

    pool::Ptr<Object> m_data;
  };

  /** base class of IOV payload wrapper (with summary)
   */
  template<typename O, typename S> 
  DataAndSummaryWrapper : public DataWrapper<O> {
  public: 
    typedef DataWrapper<O> ObjectWrapper;
    typedef typename ObjectWrapper::base base;
    typedef typename ObjectWrapper::Object Object;
    typedef typename ObjectWrapper::value_type value_type;
    typedef S Summary;
    typedef Summary summary_type;
    
    typedef DataAndSummary<value_type, summary_type> self;
    
    
    DataAndSummary(Object * obj, Summary * sum) :
      ObjectWrapper(obj), m_Summary(sum){}

    ~DataAndSummary() {
      if (m_summary.isLoaded()) delete m_summary.get();
    }    

    
    Summary const & summary() const { return *m_summary;}

    bool loadSummary() const {
      return m_summary.get();
    }

  private:

    pool::Ptr<Summary> m_summary;


  };


} // ns

#endif //Cond_PayloadWrapper_h
